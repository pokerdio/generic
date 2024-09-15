#include <Wire.h>
#include <SPI.h>
#include "SH1106.h"

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include "new_fonts.h"


const char* ssid = "COUNTDOWN-735";    // SSID of the access point
const char* password = "5432154321";  // Password for the access point

void sendWiFiCommand(int message, long data);

WiFiUDP udp;
IPAddress serverIP;    // IP of the AP
unsigned int port = 1234; // Port on the AP side
IPAddress clientIP;                // Store client's IP

bool server = false;
bool client = false;



struct {
    int message; 
    union { 
	long data;
	uint8_t ubytes[4];
	int8_t bytes[4];
    };
} incoming; 


#define PONG_PAD_WIDTH 8

struct {
    int ys; //server pad height
    int yc; //client pad height
    
    int bx; //ball x
    int by; //ball y

    int dirx;
    int diry; 

    int score_s;
    int score_c;

    int update_required; 
} pong; 


//one board has a square rotary encoder, one has a square one of a different model, hence slightly different code
//#define ROUND


#include "shhhh.h"
#include "Rotary.h"


// Node MCU
#define OLED_RESET  D0   // RESET
#define OLED_DC     D3   // Data/Command
#define OLED_CS     D8   // Chip select


//buzzer
#define TONE_PIN (D6)

bool change = false; 
int button_state = 0;
int game_selected = -1;  //rename this variable and move to countdown internal

long last_button_action = 0; 
int encoder_count = 100;
int encoder_pressed_count = 0;
bool encoder_active_rotation = false; 

int game_value_initial[9];//should be six but I made it 9 to avoid getting out of bounds in some case (should be impossible)
int game_value[9]; 
int game_target;
long game_timer; 

int best = 0;
int best_delta = 1200; 

char game_op = '+';
char game_op_list[12];  // math ops allowed for the game
char game_op_cur[12]; // rotation ops for the current press and rotate session

Rotary * rotary; 

#define TONE_MIN 100
#define TONE_MAX 2400

int state_tone = 500; 
int state_send_tone = 0; 
int state_ban_tone_traffic = 0; 

enum {
    STATE_MENU = 1, 
    STATE_GAME,
    STATE_MESSAGE,
    STATE_END_GAME,
    STATE_PONG,
    STATE_TONE
};

int state = STATE_MENU; 
int state_before_message = 0; 
int state_message = 0; 
int clk = 0; 


SH1106 display(true, OLED_RESET, OLED_DC, OLED_CS); // FOR SPI


// this has both menu IDs and packet message IDS
enum {
    MENU_FAIL = -1,
    MESSAGE_HELLO = 50, 
    MESSAGE_START = 51,
    MESSAGE_START_END = (51 + 16), 

    MENU_ASLEEP=100,
    MENU_FIRST=100,
    MENU_COUNTDOWN_SELECT,
    MENU_MESSAGE_SELECT,
    MENU_TONE_SELECT,
    MENU_PONG_SELECT,
    MENU_PONG_QUIT,

    MENU_COUNTDOWN_TIMED_SELECT,
    MENU_COUNTDOWN_FREE_SELECT,
    MENU_COUNTDOWN_20,
    MENU_COUNTDOWN_50,
    MENU_COUNTDOWN_100,
    MENU_COUNTDOWN_1000,
    MENU_COUNTDOWN_0,
    MENU_COUNTDOWN_1,
    MENU_COUNTDOWN_2,
    MENU_COUNTDOWN_3,
    MENU_COUNTDOWN_4,

    MENU_MESSAGE_QUIT,
    MENU_MESSAGE_YES,
    MENU_MESSAGE_NO,
    MENU_MESSAGE_LATER,    
    MENU_MESSAGE_COME,
    MENU_MESSAGE_WANT,
    MENU_MESSAGE_FOOD,
    MENU_MESSAGE_TOY,
    MENU_MESSAGE_WATER,
    MENU_MESSAGE_BUBBLE_WATER,
    MENU_MESSAGE_LAST, 


    MENU_LAST //keep this last, okay? 
};


int menu_option_countdown_timed = MENU_COUNTDOWN_TIMED_SELECT; 
int menu_option_countdown_max = MENU_COUNTDOWN_20; 
int menu_option_countdown_large = MENU_COUNTDOWN_2; 

int menu_state = MENU_COUNTDOWN_SELECT;


#define MENU_LENGTH (MENU_LAST - MENU_FIRST)

int menuNext(int entry) {
    switch (entry) {
    case MENU_COUNTDOWN_SELECT:
	return MENU_MESSAGE_SELECT;
    case MENU_MESSAGE_SELECT:
	return MENU_TONE_SELECT;
    case MENU_TONE_SELECT:
	return MENU_PONG_SELECT;
    case MENU_PONG_SELECT:
	return MENU_COUNTDOWN_SELECT;


    case MENU_COUNTDOWN_TIMED_SELECT:
	return MENU_COUNTDOWN_FREE_SELECT;
    case MENU_COUNTDOWN_FREE_SELECT:
	return MENU_COUNTDOWN_TIMED_SELECT;
    case MENU_COUNTDOWN_20:
	return MENU_COUNTDOWN_50;
    case MENU_COUNTDOWN_50:
	return MENU_COUNTDOWN_100;
    case MENU_COUNTDOWN_100:
	return MENU_COUNTDOWN_1000;
    case MENU_COUNTDOWN_1000:
	return MENU_COUNTDOWN_20;
    case MENU_COUNTDOWN_0:
	return MENU_COUNTDOWN_1;
    case MENU_COUNTDOWN_1:
	return MENU_COUNTDOWN_2;
    case MENU_COUNTDOWN_2:
	return MENU_COUNTDOWN_3;
    case MENU_COUNTDOWN_3:
	return MENU_COUNTDOWN_4;
    case MENU_COUNTDOWN_4:
	return MENU_COUNTDOWN_0;



    case MENU_MESSAGE_QUIT:
	return MENU_MESSAGE_YES;
    case MENU_MESSAGE_YES:
	return MENU_MESSAGE_NO;
    case MENU_MESSAGE_NO:
	return MENU_MESSAGE_LATER;
    case MENU_MESSAGE_LATER:
	return MENU_MESSAGE_COME;
    case MENU_MESSAGE_COME:
	return MENU_MESSAGE_WANT;
    case MENU_MESSAGE_WANT:
	return MENU_MESSAGE_FOOD;
    case MENU_MESSAGE_FOOD:
	return MENU_MESSAGE_TOY;
    case MENU_MESSAGE_TOY:
	return MENU_MESSAGE_WATER;
    case MENU_MESSAGE_WATER:
	return MENU_MESSAGE_BUBBLE_WATER;
    case MENU_MESSAGE_BUBBLE_WATER:
	return MENU_MESSAGE_QUIT;

    default:
	return MENU_FAIL; 
    };
    return MENU_COUNTDOWN_SELECT;  //fail 
}

int menuPrev(int entry) {
    switch(entry) {
    case MENU_COUNTDOWN_SELECT:
	return MENU_PONG_SELECT;
    case MENU_MESSAGE_SELECT:
	return MENU_COUNTDOWN_SELECT;
    case MENU_TONE_SELECT:
	return MENU_MESSAGE_SELECT;
    case MENU_PONG_SELECT:
	return MENU_TONE_SELECT;



    case MENU_COUNTDOWN_TIMED_SELECT:
	return MENU_COUNTDOWN_FREE_SELECT;
    case MENU_COUNTDOWN_FREE_SELECT:
	return MENU_COUNTDOWN_TIMED_SELECT;
    case MENU_COUNTDOWN_20:
	return MENU_COUNTDOWN_1000;
    case MENU_COUNTDOWN_50:
	return MENU_COUNTDOWN_20;
    case MENU_COUNTDOWN_100:
	return MENU_COUNTDOWN_50;
    case MENU_COUNTDOWN_1000:
	return MENU_COUNTDOWN_100;
    case MENU_COUNTDOWN_0:
	return MENU_COUNTDOWN_4;
    case MENU_COUNTDOWN_1:
	return MENU_COUNTDOWN_0;
    case MENU_COUNTDOWN_2:
	return MENU_COUNTDOWN_1;
    case MENU_COUNTDOWN_3:
	return MENU_COUNTDOWN_2;
    case MENU_COUNTDOWN_4:
	return MENU_COUNTDOWN_3;


    case MENU_MESSAGE_QUIT:
	return MENU_MESSAGE_BUBBLE_WATER;
    case MENU_MESSAGE_YES:
	return MENU_MESSAGE_QUIT;
    case MENU_MESSAGE_NO:
	return MENU_MESSAGE_YES;
    case MENU_MESSAGE_LATER:
	return MENU_MESSAGE_NO;
    case MENU_MESSAGE_COME:
	return MENU_MESSAGE_LATER;
    case MENU_MESSAGE_WANT:
	return MENU_MESSAGE_COME;
    case MENU_MESSAGE_FOOD:
	return MENU_MESSAGE_WANT;
    case MENU_MESSAGE_TOY:
	return MENU_MESSAGE_FOOD;
    case MENU_MESSAGE_WATER:
	return MENU_MESSAGE_TOY;
    case MENU_MESSAGE_BUBBLE_WATER:
	return MENU_MESSAGE_WATER;

    }
    return MENU_COUNTDOWN_SELECT;  //fail 
}

const char* menuString(int entry) {
    switch (entry) { 
    case MENU_COUNTDOWN_SELECT:
	return "Countdown";
    case MENU_MESSAGE_SELECT:
	return "Message";
    case MENU_TONE_SELECT:
	return "Beep";
    case MENU_PONG_SELECT:
	return "Pong";

    case MENU_COUNTDOWN_TIMED_SELECT:
	return "Timed Contest";
    case MENU_COUNTDOWN_FREE_SELECT:
	return "Free Play";
    case MENU_COUNTDOWN_20:
	return "20 MAX";
    case MENU_COUNTDOWN_50:
	return "50 MAX";
    case MENU_COUNTDOWN_100:
	return "99 MAX";
    case MENU_COUNTDOWN_1000:
	return "999 MAX";
    case MENU_COUNTDOWN_0:
	return "6 small";
    case MENU_COUNTDOWN_1:
	return "1 large";
    case MENU_COUNTDOWN_2:
	return "2 large";
    case MENU_COUNTDOWN_3:
	return "3 large";
    case MENU_COUNTDOWN_4:
	return "4 large";


    case MENU_MESSAGE_QUIT:
	return "<<<";
    case MENU_MESSAGE_YES:
	return "DA";
    case MENU_MESSAGE_NO:
	return "NU";
    case MENU_MESSAGE_LATER:
	return "MAI TARZIU";
    case MENU_MESSAGE_COME:
	return "VINO!";
    case MENU_MESSAGE_WANT:
	return "VREAU!";
    case MENU_MESSAGE_FOOD:
	return "MANCARE";
    case MENU_MESSAGE_TOY:
	return "JUCARIE";
    case MENU_MESSAGE_WATER:
	return "APA";
    case MENU_MESSAGE_BUBBLE_WATER:
	return "APA CU BULE";
    }
    return "";
}

void menuCountDownStart(void) {
    int m = MESSAGE_START;
    switch(menu_option_countdown_max) {
    case MENU_COUNTDOWN_20:
	break;
    case MENU_COUNTDOWN_50:
	m += 1; 
	break;
    case MENU_COUNTDOWN_100:
	m += 2; 
	break;
    case MENU_COUNTDOWN_1000:
	m += 3 + (menu_option_countdown_large - MENU_COUNTDOWN_0); //values 3..7 inclusive are 
	break;
    }
    if (menu_option_countdown_max) {
	m += 8; 
    }

    int seed = millis(); 
    sendWiFiCommand(m, seed);
    gameStart(m, seed);

    menu_state = MENU_COUNTDOWN_SELECT;
}

void messageSend(int entry) {
    if (state != STATE_MESSAGE) { 
	state_before_message = state;
    }
    state = STATE_MESSAGE;
    noTone(TONE_PIN);
    state_message = entry; 
}

void pongBallReset(void) {
    pong.dirx = 1 - random(0, 2) * 2;
    pong.diry = 1 - random(0, 2) * 2;

    pong.bx = 64;
    pong.by = 32;
}

void menuPongStart(void) {
    pongBallReset(); 

    pong.ys = 32;  //server
    pong.yc = 32;  //client

    state = STATE_PONG; 
    pong.score_s = 0;
    pong.score_c = 0; 
}


void pongSend(int send_ball) {
    pong.update_required = 0; 
    if (server) {
	incoming.bytes[0] = pong.ys;
	incoming.bytes[1] = pong.score_c;//server keeps track of own goals, which raise score_c
    } else {
	incoming.bytes[0] = pong.yc;
	incoming.bytes[1] = pong.score_s;//client keeps track of own goals, which raise score_s
    }

    if (!send_ball) {
	incoming.bytes[2] = -128;
	incoming.bytes[3] = -128;
	sendWiFiCommand(MENU_PONG_SELECT, incoming.data);
	return; 
    }

    if (pong.dirx > 0) {
	incoming.bytes[2] = pong.bx;
    }  else {
	incoming.bytes[2] = -pong.bx;
    }
    if (pong.diry > 0) {
	incoming.bytes[3] = pong.by;
    }  else {
	incoming.bytes[3] = -pong.by;
    }

    sendWiFiCommand(MENU_PONG_SELECT, incoming.data);
}

void shortBeep(void) {
    tone(TONE_PIN, 1200, 20);
}

void longBeep(void) {
    tone(TONE_PIN, 1200, 150);
}

void pongRecv(void) {
    int beep = 0; 
    if (client) {
	pong.ys = incoming.bytes[0];
	if (pong.score_c != incoming.bytes[1]) {
	    pong.score_c = incoming.bytes[1];
	    longBeep();
	    beep = 1; 
	}
    } else {
	pong.yc = incoming.bytes[0];
	if (pong.score_s != incoming.bytes[1]) {
	    pong.score_s = incoming.bytes[1];
	    longBeep();
	    beep = 1; 
	}
    }
    char old_dirx = pong.dirx;
    if (incoming.bytes[2] > -128)  {
	pong.bx = abs((int)incoming.bytes[2]);
	pong.by = abs((int)incoming.bytes[3]);

	if ((client && pong.bx < 80) || (server && pong.bx > 40)) {
	    pong.dirx = (incoming.bytes[2] > 0) ? 1 : -1; 
	    pong.diry = (incoming.bytes[3] > 0) ? 1 : -1; 
	}
	if (!beep && old_dirx != pong.dirx) {
	    shortBeep();
	}
    }
}

void menuAction(int entry) {
    switch (entry) {
    case MENU_PONG_SELECT:
	menuPongStart();
	pongSend(1); 
	break;
    case MENU_COUNTDOWN_SELECT:
	menu_state = MENU_COUNTDOWN_TIMED_SELECT;
	break;
    case MENU_TONE_SELECT:
	state = STATE_TONE; 
	tone(TONE_PIN, state_tone);
	sendWiFiCommand(MENU_TONE_SELECT, state_tone);
	state_ban_tone_traffic = 0; 
	break;
    case MENU_MESSAGE_SELECT:
	menu_state = MENU_MESSAGE_YES;
	break;
    case MENU_COUNTDOWN_TIMED_SELECT:
	menu_option_countdown_timed = MENU_COUNTDOWN_TIMED_SELECT; 
	menu_state = menu_option_countdown_max; 
	break;
    case MENU_COUNTDOWN_FREE_SELECT:
	menu_option_countdown_timed = MENU_COUNTDOWN_FREE_SELECT; 
	menu_state = menu_option_countdown_max; 
	break;
    case MENU_COUNTDOWN_20:
    case MENU_COUNTDOWN_50:
    case MENU_COUNTDOWN_100:
	menuCountDownStart();
	menu_option_countdown_max = entry;
	menu_state = MENU_COUNTDOWN_SELECT;
	break;
    case MENU_COUNTDOWN_1000:
	menu_option_countdown_max = entry; 
	menu_state = menu_option_countdown_large; 
	break;
    case MENU_COUNTDOWN_0:
    case MENU_COUNTDOWN_1:
    case MENU_COUNTDOWN_2:
    case MENU_COUNTDOWN_3:
    case MENU_COUNTDOWN_4:
	menu_option_countdown_large = entry;
	menuCountDownStart();
	break;

    case MENU_MESSAGE_QUIT:
	menu_state = MENU_MESSAGE_SELECT;
	break;
    case MENU_MESSAGE_YES:
    case MENU_MESSAGE_NO:
    case MENU_MESSAGE_LATER:
    case MENU_MESSAGE_COME:
    case MENU_MESSAGE_WANT:
    case MENU_MESSAGE_FOOD:
    case MENU_MESSAGE_TOY:
    case MENU_MESSAGE_WATER:
    case MENU_MESSAGE_BUBBLE_WATER:
	messageSend(entry);
	sendWiFiCommand(entry, 0);
	break; 
    default:
	menu_state = MENU_COUNTDOWN_SELECT; // menu fail state should never happen
	break;
    };
}

int getPos(void);

void encoderReset(void) {
    encoder_pressed_count = -1; 
}

int encode(int n, int div) {
    if (div <= 1) {
	return 0; 
    } else {
	n = n % div;
	if (n < 0) {
	    n += div; 
	}
    }
    return n; 
}


void p(SH1106 &display, int y, const String & s) {
    display.setColor(WHITE);
    display.setTextAlignment(TEXT_ALIGN_RIGHT);
    display.setFont(ArialMT_Plain_10);
    display.drawString(128, y, s);
}


void setState(int new_state) {
    if (state != new_state) {
	state = new_state;
	change = true;
	clk = 0; 
    }
}

void gameOverlay(SH1106 &display) {
    if (game_timer > 0) {
	int delta = (game_timer - millis()) / 1000;
	if (delta <= 120) {
	    display.setColor(WHITE);
	    display.setTextAlignment(TEXT_ALIGN_RIGHT);
	    display.setFont(ArialMT_Plain_10);
	    display.drawString(128, 48, String(delta));
	}
    }
    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.setFont(SansSerif_bold_14);

    display.setColor(WHITE);
    int w = display.getStringWidth(String(game_target)) + 4;
    display.fillRect(8, 38, w, 16);
    display.setColor(BLACK);
    display.drawString(8 + w / 2, 38, String(game_target)); 

    if (best > 0) { 
	display.setColor(WHITE);
	display.setFont(ArialMT_Plain_10);
	display.drawString(8 + w / 2, 53, String(best));
    }

    display.setColor(WHITE);
#define NOP 6
    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.setFont(ArialMT_Plain_24);
    display.drawString(70, 40, String(game_op));
}


void drawFrameMenu(SH1106 &display) {
    static char txt[] = "COUNTDOWN";

    display.clear();
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.setFont(SansSerif_bold_14);


    display.drawString(8, 4, String(menuString(menuPrev(menu_state))));

    display.drawRect(6, 22, display.getStringWidth(String(menuString(menu_state))) + 4, 18);
    display.drawString(8, 24, String(menuString(menu_state)));

    if (menuPrev(menu_state) != menuNext(menu_state)) {
	display.drawString(8, 44, String(menuString(menuNext(menu_state))));
    }
}

void drawMessage(SH1106 &display) {
    display.clear();
    display.setTextAlignment(TEXT_ALIGN_LEFT);
    display.setFont(SansSerif_bold_14);

    display.drawString(4, 24, String(menuString(state_message)));
}


void drawOption (SH1106 &display, const String& text, const String &subtext, int selected, int active, int row, int col) {
    int x = (128 * col / 3) + 1;
    int y = (64 * row / 3) + 1;
    int w = 128 / 3 - 2;
    int h = 64 / 3 - 2; 

    if (subtext.length() > 0) {
	display.setTextAlignment(TEXT_ALIGN_CENTER);
	display.setFont(SansSerif_bold_14);
	display.setColor(WHITE);
	display.drawString(x + w / 2, y, text);

	display.setFont(ArialMT_Plain_10);
	display.drawString(x + w / 2, y + 10, subtext);
    } else {
	y = 18 * row + 1;
	if (row == 2) {
	    y += 4; 
	}
	h = 16; 

	display.setTextAlignment(TEXT_ALIGN_CENTER);
	if (text.length() > 3) {
	    display.setFont(ArialMT_Plain_10);	    
	} else {
	    display.setFont(SansSerif_bold_14);
	}
	display.setColor(WHITE);
	int i = row * 3 + col; 

	if (state == STATE_GAME) {
	    //hack to blink the text when the player made the target during the game
	    if (i > 5 || !(game_value[i] == game_target && (millis() % 750 > 375))) {
		display.drawString(x + w / 2, y + 2, text);
	    }
	} 
    }
    if (selected) {
	int wide = 6;
	int narrow = 2;
	display.fillRect(x, y, wide, narrow);
	display.fillRect(x, y, narrow, wide);

	display.fillRect(x + w - wide + 2, y, wide, narrow);
	display.fillRect(x + w, y, narrow, wide);

	display.fillRect(x, y + h, wide, narrow);
	display.fillRect(x, y + h - wide, narrow, wide);

	display.fillRect(x + w - wide + 2, y + h, wide, narrow);
	display.fillRect(x + w, y + h - wide, narrow, wide);
    }
    if (active) {
	display.drawRect(x + 1, y + 1, w - 1, h - 1);
    }
}

void gameInit(int max, int large_count) {
    int i; 
    large_count = (large_count < 0) ? 0 : large_count;
    large_count = (large_count > 4) ? 4 : large_count;
    switch(max) {
    case 20:
	for (i=0 ; i<6 ; ++i) {
	    game_value_initial[i] = random(1, 10);
	}
	game_target = random(10, 21);
	strcpy(game_op_list, "+-");
	break;
    case 50:
    case 100:
	game_value_initial[0] = 10 + 5 * random (0, 4);
	for (i=1 ; i<6 ; ++i) {
	    game_value_initial[i] = random(1, 10);
	}
	game_target = random(20, max);
	strcpy(game_op_list, "+-*");
	break;
    default: ///1000
	int large = 0;
	switch(large_count) {
	case 1:
	    large = 1 << random(4);
	    break;
	case 3:
	    large = 15 - (1 << random (4));
	    break;
	case 4:
	    large = 15; 
	    break;
	case 2:
	    switch(random(6)) {
	    case 0:
		large = 1 + 2; 
		break;
	    case 1:
		large = 1 + 4; 
		break;
	    case 2:
		large = 1 + 8;
		break;
	    case 3:
		large = 2 + 4;
		break;
	    case 4:
		large = 2 + 8;
		break;
	    case 5:
		large = 4 + 8;
		break;
	    }
	    break;
	}
	int j = 0; 
	for (i=0 ; i<4 ; ++i) {
	    if (large & (1 << i)) {
		game_value_initial[j++] = 25 * (1 + i);
	    }
	}
	for (i=j ; i<6 ; ++i) {
	    game_value_initial[i] = random(1, 10);
	}
	strcpy(game_op_list, "+-*/");
	game_target = random(101, 1000);
    }
    for (i=0 ; i<6 ; ++i) {
	game_value[i] = game_value_initial[i];
    }
    game_op = '+';
}

void gameStart(int message, int seed) {
    int small_count = 0;
    int type; 
    int timed;

    if (message < MESSAGE_START || message >= MESSAGE_START_END) {
	return;
    }
    message -= MESSAGE_START;

    setState(STATE_GAME);
    type = encode(message, 8);
    timed = (message >= 8); 

    if (seed >= 0) { 
	randomSeed(seed);
    } else {
	randomSeed(millis());
    }
    switch (type) {
    case 0:
	gameInit(20, 0);
	break;
    case 1:
	gameInit(50, 0);	
	break;
    case 2:
	gameInit(100, 0);
	break;
    case 3:
    case 4:
    case 5:
    case 6:
    case 7:
	gameInit(1000, type - 3);
	break;
    }
    if (timed) {
	game_timer = millis() + 91000;
    } else {
	game_timer = 0;
    }

    noTone(TONE_PIN);
    encoderReset(); 
    encoder_active_rotation = false;
    encoder_count = 0; 
    game_selected = -1; 

    best = 0;
    best_delta = 1200; 
}


void drawFrameGame(SH1106 &display) {
    int pos = getPos();
    String empty = "";

    display.clear();
//    p(display, 44, String (digitalRead(ROT_A)) + String (digitalRead(ROT_B)) + String (digitalRead(ROT_C)));
    for (int i=0 ; i<6 ; ++i) {
	if (game_value[i] <= 0) {
	    continue; 
	}
	drawOption (display, String(game_value[i]), empty, pos == i, i == game_selected, i / 3, i % 3);
    }
    gameOverlay(display);
}


void updateBest() {
    int i; 
    for (i=0 ; i<6 ; ++i) {
	if(game_value[i] < 1) {
	    continue; 
	}
	int candidate = abs(abs(game_value[i]) - game_target);
	if (candidate < best_delta) {
	    best_delta = candidate;
	    best = game_value[i];
	}
    }
}


void drawTone(SH1106 &display) {
    display.clear();
    display.setColor(WHITE);

    double m = log(TONE_MIN);
    double M = log(TONE_MAX);
    double x = log(state_tone);

    int proc = (int)100.0 * (x - m) / (M - m);

    display.drawRect(14, 30, 101, 5);
    display.fillRect(15, 31, proc, 4);

    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.drawString(64, 40, String(proc));
}

void drawFrameEndGame(SH1106 &display) {
    display.clear();
//    p(display, 54, String (digitalRead(ROT_A)) + String (digitalRead(ROT_B)) + String (digitalRead(ROT_C)));
    display.setColor(WHITE);
    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.setFont(ArialMT_Plain_24);
    display.drawString(54, 18, String(best));

    display.setFont(ArialMT_Plain_10);
    display.drawString(54, 45, String(game_target));
    int delta = best - game_target; 
    if (delta != 0) {
	display.drawString(90, 25, (delta > 0) ? String("+") + String(delta) : String(delta));
    } else {
	display.drawString(90, 25, String("!!!"));
    }
}

void drawFrameDebug(SH1106 &display) {
    return;
    display.setColor(WHITE);
    display.setTextAlignment(TEXT_ALIGN_RIGHT);
    display.setFont(ArialMT_Plain_10);
    display.drawString(125, 50, String(incoming.data) + String(" ") + 
		       String((int)incoming.bytes[2]) + String(" ") + 
		       String(String((int)incoming.bytes[3])));
}


ICACHE_RAM_ATTR void detectRotation() {
    int dir = rotary->process(); 
    int n = 0, m; 
    int old; 
    change = true; 
    switch (state) {
    case STATE_PONG:
	if (DIR_CW == dir) {
	    m = -2;
	} else if (DIR_CCW == dir) {
	    m = 2;
	} else {
	    break;
	}
	if (server) {
	    old = pong.ys; 
	    pong.ys += m;
	    if (pong.ys > 63 - PONG_PAD_WIDTH) {
		pong.ys = 63 - PONG_PAD_WIDTH;
	    }
	    if (pong.ys < PONG_PAD_WIDTH) {
		pong.ys = PONG_PAD_WIDTH;
	    }
	    if (pong.ys != old) {
		pong.update_required = 1; 
	    }
	} else {
	    old = pong.yc; 
	    pong.yc += m;	    
	    if (pong.yc > 63 - PONG_PAD_WIDTH) {
		pong.yc = 63 - PONG_PAD_WIDTH;
	    }
	    if (pong.yc < PONG_PAD_WIDTH) {
		pong.yc = PONG_PAD_WIDTH;
	    }
	    if (pong.yc != old) {
		pong.update_required = 1; 
	    }
	}
	break;	
    case STATE_TONE:  
	if (DIR_CW == dir) {
	    state_tone = (int)state_tone * 1.1;
	    if (state_tone > TONE_MAX) {
		state_tone = TONE_MAX;
	    }
	    state_send_tone = 1; 
	} else if (DIR_CCW == dir) {
	    state_tone = (int)state_tone * 0.9;
	    if (state_tone < TONE_MIN) {
		state_tone = TONE_MIN;
	    }
	    state_send_tone = 1; 
	}
	break; 
    case STATE_MENU:
	if (DIR_CW == dir) {
	    menu_state = menuNext(menu_state);
	} else if (DIR_CCW == dir) {
	    menu_state = menuPrev(menu_state);
	}
	break;
    case STATE_GAME:
	if (button_state) { 
	    if (encoder_pressed_count < 0) { 
		n = strlen(game_op_list);
		strcpy(game_op_cur, game_op_list);

		game_op_cur[n++] = 'Q';
		game_op_cur[n++] = 'R'; 


		m = 1; 
		for (n=0 ; game_op_list[n] ; ++n) {
		    if (game_op_list[n] != game_op) {
			game_op_cur[m++] = game_op_list[n];
		    }
		}
		game_op_cur[0] = game_op; 
		encoder_pressed_count = 0; 
	    }

	    if (DIR_CW == dir) {
		encoder_pressed_count = encode(1 + encoder_pressed_count, strlen(game_op_cur));
		encoder_active_rotation = true; 
	    } else if (DIR_CCW == dir) {
		encoder_pressed_count = encode(encoder_pressed_count - 1, strlen(game_op_cur));
		encoder_active_rotation = true; 
	    }
	    game_op = game_op_cur[encoder_pressed_count];
	} else  {
	    if (DIR_CW == dir) {
		encoder_count++;
	    } else if (DIR_CCW == dir) {
		encoder_count--;
	    }
	}
	break;
    default:
	if (DIR_CW == dir) {
	    encoder_count++;
	} else if (DIR_CCW == dir) {
	    encoder_count--;
	}
    }
}

int getPos(void) {
    int n = 0;
    int i;
    for (i=0 ; i<6 ; ++i) {
	if (game_value[i] > 0) {
	    n++; 
	}
    }
    if (n == 1) {
	for (i=0 ; i<6 ; ++i) {
	    if (game_value[i] > 0) {
		return i;
	    }
	}
    }
    if (n == 0) {
	return 0;
    }

    int x = encode(encoder_count, n);

    for (i=0 ; i<6 ; ++i) {
	if (game_value[i] > 0) {
	    if (x-- <= 0) {
		return i;
	    }
	}
    }
    return 0;
}

void delSelected() {
    if (game_selected < 0) {
	return;
    }
    int old_pos = getPos();
    game_value[game_selected] = 0; 
    game_selected = -1; 

    int n;
    for (int i=0 ; i<6 ; ++i) {
	n += (game_value[i] > 0);
    }
    if (n == 1) {
	game_op = 'R';
    }

    for (encoder_count=0 ; encoder_count < 6 ; ++encoder_count) {
	if (getPos() == old_pos) {
	    return;
	}
    }
}


#define ACTION (button_state && !new_button_state &&  (millis() - last_button_action > 50))

void detectPush() {
    int new_button_state = !digitalRead(ROT_C);
    int i;

    if (!new_button_state) {
	encoderReset(); 
    }

    change = true;  
    if (ACTION) {
	switch (state) {
	case STATE_PONG:
	    noTone(TONE_PIN);
	    state = STATE_MENU;
	    sendWiFiCommand(MENU_PONG_QUIT, 0); 
	    delay(50);
	    sendWiFiCommand(MENU_PONG_QUIT, 0); 
	    break;
	case STATE_TONE:
	    noTone(TONE_PIN);
	    state = STATE_MENU;
	    state_ban_tone_traffic = 1; 
	    break;
	case STATE_MENU:
	    menuAction(menu_state);
	    break;
	case STATE_MESSAGE:
	    state = state_before_message;
	    break; 
	case STATE_GAME:
	    last_button_action = millis(); 

	    switch(game_op) {
	    case 'R':
		game_selected = -1; 
		for (i=0 ; i<6 ; ++i) {
		    game_value[i] = game_value_initial[i];
		}
		game_op = '+';
		break;
	    case 'Q':
		setState(STATE_END_GAME);
		clk = 0; 
		break;
	    case '+':
	    case '-':
	    case '*':
	    case '/':
		int pos = getPos();
		if (game_selected < 0) {
		    game_selected = pos;
		    break; 
		} else if (game_selected == pos) {
		    if (!encoder_active_rotation) {
			game_selected = -1;
		    }
		    break; 
		}

		switch(game_op) {
		case '+':
		    game_value[pos] += game_value[game_selected];
		    delSelected();
		    break;
		case '-':
		    game_value[pos] = abs(game_value[game_selected] - game_value[pos]);
		    delSelected();
		    break;
		case '*':
		    game_value[pos] = game_value[game_selected] * game_value[pos];
		    delSelected();
		    break;
		case '/':
		    if (game_value[pos] % game_value[game_selected] == 0) {
			game_value[pos] = game_value[pos] / game_value[game_selected];
			delSelected();
		    } else if (game_value[game_selected] % game_value[pos] == 0) {
			game_value[pos] = game_value[game_selected] / game_value[pos];
			delSelected();
		    }
		    break;
		}
		updateBest();
		break;
	    }
	    break;
	case STATE_END_GAME:
	    last_button_action = millis(); 
	    setState(STATE_MENU);
	    menu_state = MENU_COUNTDOWN_SELECT;
	    clk = 0; 
	    break;
	}
    }
    if (!new_button_state) {
	last_button_action = millis(); 
	encoder_active_rotation = false;
    }
    button_state = new_button_state; 
}

#undef ACTION


void setup() {

    delay(10);

    Serial.begin(9600);
    Serial.println("connecting");

    pinMode (ROT_A,INPUT);
    pinMode (ROT_B,INPUT);
    pinMode (ROT_C,INPUT_PULLUP);
//    digitalWrite(ROT_C, 1);

    rotary = new Rotary(ROT_A, ROT_B);

    display.init();
    display.flipScreenVertically();
    display.displayOn();

    attachInterrupt(digitalPinToInterrupt(ROT_A), detectRotation, CHANGE);
    attachInterrupt(digitalPinToInterrupt(ROT_B), detectRotation, CHANGE);


    // try to Connect to the Access Point
    WiFi.begin(ssid, password);
    int i; 
    const int ntry = 40; 
    for (i=0 ; (WiFi.status() != WL_CONNECTED) && i<ntry ; ++i) {
	delay(200);
	Serial.print(".");
    }
    if (i < ntry) {
	server = false;
	client = true; 
	Serial.println("Connected to AP");

	// Get the IP of the AP (which will be softAPIP)
	serverIP = IPAddress(192, 168, 4, 1);

	// Start UDP communication
	udp.begin(port);
	sendWiFiCommand(MESSAGE_HELLO, 0); // so the server can get my ip
    } else {
	// Set up the Access Point
	server = true;
	client = false; 

	WiFi.mode(WIFI_AP);
	WiFi.softAP(ssid, password);
	serverIP = WiFi.softAPIP();
	Serial.print("AP IP address: ");
	Serial.println(serverIP);

	// Begin listening on UDP port
	udp.begin(port);
	Serial.printf("Listening on UDP port %d\n", port);
    }

    pinMode(TONE_PIN, OUTPUT);
}

void startIncoming(void) {
    if (incoming.message == MENU_PONG_SELECT && state != STATE_PONG)  {
	menuPongStart(); 
	pongRecv(); 
	noTone(TONE_PIN);
	return;
    }
    
    if (incoming.message == MENU_TONE_SELECT && !state_ban_tone_traffic) {
	state_tone = incoming.data;
	tone(TONE_PIN, state_tone);
	state = STATE_TONE; 
	return; 
    }
    if(incoming.message >= MESSAGE_START && incoming.message < MESSAGE_START_END) {
	gameStart(incoming.message, incoming.data);
    }
    if(incoming.message >= MENU_MESSAGE_YES && incoming.message < MENU_MESSAGE_LAST) {
	messageSend(incoming.message);
    }
}


void listenWiFiCommand() {
    int packetSize = udp.parsePacket();
    if (packetSize <= 0) {
	return;
    }
    udp.read((char*)&incoming, sizeof(incoming));    
    if (server) {
	// Print the received packet
	Serial.printf("server received packet: %d %ld\n", incoming.message, incoming.data);
	// Store client IP and port from the packet metadata
	clientIP = udp.remoteIP();

	switch (state) {
	case STATE_PONG:
	    if (incoming.message == MENU_PONG_SELECT) {
		pongRecv();
	    }
	    if (incoming.message == MENU_PONG_QUIT) {
		state = STATE_MENU;
		noTone(TONE_PIN);
		menu_state = MENU_PONG_SELECT;
	    }
	    break;
	case STATE_MENU:
	case STATE_MESSAGE:
	case STATE_TONE:
	    if (incoming.message == MENU_PONG_QUIT) {
		break; 
	    }
	    startIncoming();
	    break;
	}
    }
    if (client) {
	Serial.printf("client received packet: %d %ld\n", incoming.message, incoming.data);

	switch (state) {
	case STATE_PONG:
	    if (incoming.message == MENU_PONG_SELECT) {
		pongRecv();
	    }
	    if (incoming.message == MENU_PONG_QUIT) {
		state = STATE_MENU;
		noTone(TONE_PIN);
		menu_state = MENU_PONG_SELECT;
	    }
	    break;
	case STATE_MENU:
	case STATE_MESSAGE:
	case STATE_TONE:
	    if (incoming.message == MENU_PONG_QUIT) {
		break; 
	    }
	    startIncoming(); 
	    break;
	}
    }

}

void sendWiFiCommand(int message, long data) {
    int ret; 
    incoming.message = message;
    incoming.data = data;

    if (client) { 
	Serial.printf("client sending packet: %d %ld\n", message, data);
	ret = udp.beginPacket(serverIP, port);
    } else {
	Serial.printf("server sending packet: %d %ld\n", message, data);
	ret = udp.beginPacket(clientIP, port);	
    }
    if (!ret) {
	Serial.printf("beginPacket fail\n");
	return;
    }

    udp.write((char*)&incoming, sizeof(incoming));
    if (!udp.endPacket()) {
	switch(WiFi.status()) {
	case WL_CONNECTED:
	    Serial.printf("endPacket fail; status connected\n");
	    break;
	case WL_CONNECT_FAILED:
	    Serial.printf("endPacket fail; status connect failed \n");
	    break;
	case WL_NO_SSID_AVAIL:
	    Serial.printf("endPacket fail; status no ssid avail\n");
	    break;
	case WL_DISCONNECTED:
	    Serial.printf("endPacket fail; status disconnected\n");
	    break;
	case WL_CONNECTION_LOST:
	    Serial.printf("endPacket fail; status connection lost\n");
	    break;
	default:
	    Serial.printf("endPacket fail; status other\n");
	    break;
	}
    } 
}

void pongTick () {
    if (pong.dirx == 1 && pong.bx < 127) {
	pong.bx++; 
    }
    if (pong.dirx == -1 && pong.bx > 0) {
	pong.bx--; 
    }
    if (pong.diry == 1 && pong.by < 63) {
	pong.by++; 
    }
    if (pong.diry == -1 && pong.by > 0) {
	pong.by--; 
    }

    if (pong.by <= 0) {
	pong.diry = 1; 
    }
    if (pong.by >= 63) {
	pong.diry = -1; 
    }

    if (server) {
	if ((pong.dirx == -1) && (pong.bx == 2) && abs((int)pong.by - (int)pong.ys) <= PONG_PAD_WIDTH) { //boink
	    pong.dirx = 1; 
	    shortBeep(); 
	    pongSend(1); 
	} else if (pong.bx <= 0) {
	    pong.score_c++; 
	    pongBallReset();
	    longBeep(); 
	    pongSend(1);
	}
	if (((pong.bx == 4) || (pong.bx == 8) || (pong.bx == 68)) && pong.dirx == 1) {
	    pongSend(1);  // redundancy sends
	}
    } else if (client) {
	if ((pong.dirx == 1) && (pong.bx == 125) && abs((int)pong.by - (int)pong.yc) <= PONG_PAD_WIDTH) { //boink
	    pong.dirx = -1; 
	    shortBeep(); 
	    pongSend(1); 
	} else if (pong.bx >= 127) {
	    pong.score_s++; 
	    pongBallReset();
	    longBeep(); 
	    pongSend(1); 
	}
	if (((pong.bx == 122) || (pong.bx == 116) || (pong.bx == 58)) && pong.dirx == -1) {
	    pongSend(1);  // redundancy sends
	}
    }
}

void drawPong (SH1106 &display) {
    display.clear();     
    display.fillRect(2, pong.ys - PONG_PAD_WIDTH, 1, PONG_PAD_WIDTH * 2);
    display.fillRect(125, pong.yc - PONG_PAD_WIDTH, 1, PONG_PAD_WIDTH * 2);    
    display.fillRect(pong.bx - 1, pong.by - 1, 3, 3);

    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.setFont(ArialMT_Plain_10);
    display.drawString(20, 3, String((int)pong.score_s));
    display.drawString(107, 3, String((int)pong.score_c));
}

void loop() {
    detectPush();
    listenWiFiCommand();

    if (state_send_tone) {
	tone(TONE_PIN, state_tone);
	sendWiFiCommand(MENU_TONE_SELECT, state_tone);
	state_send_tone = 0;
    }

    switch(state) {
    case STATE_PONG:
	pongTick();
	pongTick();

	if (pong.update_required) {
	    pongSend(0); 
	}
	drawPong(display); 
	break;
    case STATE_TONE:
	drawTone (display);
	break;
    case STATE_MENU:
	drawFrameMenu(display);
	break;
    case STATE_MESSAGE:
	drawMessage(display);
	break; 
    case STATE_GAME:
	drawFrameGame(display);
	if (game_timer > 0 && game_timer < millis ()) {
	    setState(STATE_END_GAME);
	}
	break;
    case STATE_END_GAME:
	drawFrameEndGame(display);
	break;
    }
    change = false; 

    drawFrameDebug(display);
    display.display();
    clk++;
    delay(20);
}

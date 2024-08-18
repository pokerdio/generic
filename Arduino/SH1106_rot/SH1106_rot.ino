#include <Wire.h>
#include <SPI.h>
#include "SH1106.h"

#include <ESP8266WiFi.h>
#include <WiFiUdp.h>
#include "new_fonts.h"


const char* ssid = "COUNTDOWN";    // SSID of the access point
const char* password = "543210";  // Password for the access point

void sendWiFiCommand(int message, long seed);

WiFiUDP udp;
IPAddress serverIP;    // IP of the AP
unsigned int port = 1234; // Port on the AP side
IPAddress clientIP;                // Store client's IP

bool server = false;
bool client = false;


#define MESSAGE_HELLO  99
#define MESSAGE_START_0 100
#define MESSAGE_START_1 101
#define MESSAGE_START_2 102
#define MESSAGE_START_3 103
#define MESSAGE_START_4 104

struct incoming_t {
    int message; 
    long seed; 
} incoming; 
 

//one board has a square rotary encoder, one has a square one of a different model, hence slightly different code
//#define ROUND


#include "shhhh.h"
#include "Rotary.h"


// Node MCU
#define OLED_RESET  D0   // RESET
#define OLED_DC     D3   // Data/Command
#define OLED_CS     D8   // Chip select

bool change = false; 
int button_state = 0;
int game_selected = -1; 

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

#define STATE_INTRO 1
#define STATE_GAME_SELECT 2
#define STATE_GAME 3
#define STATE_END_GAME 4

int state = STATE_INTRO; 
int clk = 0; 


SH1106 display(true, OLED_RESET, OLED_DC, OLED_CS); // FOR SPI
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


void drawFrameIntro(SH1106 &display) {
    static char txt[] = "COUNTDOWN";

    display.clear();
    display.setTextAlignment(TEXT_ALIGN_CENTER);
    display.setFont(SansSerif_bold_14);

    int w = 0;
    int repeat = 1; 

    for (int i=0 ; txt[i] ; ++i) {
	String s = String(txt[i]);
	int sw = display.getStringWidth(s);

	int st; 
	if (clk < 50) {
	    st = clk - i;
	    st = (st < 0) ? 0 : st;
	} else {
	    st = i + 80 - clk;
	    st = (st < 0) ? 0 : st;
	}
	int delta = (st * 2 >= sw + 1) ? (sw + 1) / 2 : st;
	display.setColor(WHITE);
	display.fillRect(w + sw / 2 - delta, 18, delta * 2, 20);
		
	display.setColor(BLACK);
	display.drawString(w + sw / 2, 20, s);

	w += sw + 2;
    }
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
	} else if (state == STATE_GAME_SELECT) {
	    display.drawString(x + w / 2, y + 2, text);	    
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

void drawFrameSelect(SH1106 &display) {
    int sel = encode(encoder_count, 9);
    String empty = "";

    display.clear();
//    p(display, 54, String (digitalRead(ROT_A)) + String (digitalRead(ROT_B)) + String (digitalRead(ROT_C)));

    drawOption (display, String("999"), String("-"), sel == 0, 0, 0, 0);
    drawOption (display, String("999"), String("0/6"), sel == 1, 0, 0, 1);
    drawOption (display, String("999"), String("1/5"), sel == 2, 0, 0, 2);
    drawOption (display, String("999"), String("2/4"), sel == 3, 0, 1, 0);

    drawOption (display, String("999"), String("3/3"), sel == 4, 0, 1, 1);
    drawOption (display, String("999"), String("4/2"), sel == 5, 0, 1, 2);

    drawOption (display, String("20"), empty, sel == 6, 0, 2, 0);
    drawOption (display, String("50"), empty, sel == 7, 0, 2, 1);
    drawOption (display, String("100"), empty, sel == 8, 0, 2, 2);
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

void gameStart(int type, int seed) {
    int small_count = 0;
    int count = 6; 
    setState(STATE_GAME);
    type = encode(type, 9); 

    if (seed >= 0) { 
	randomSeed(seed);
    } else {
	randomSeed(millis());
    }
    if (type < 0) {
	type = encode(encoder_count, 9);
    }

    game_timer = millis() + 91000;

    switch (type) {
    case 0:
	gameInit(1000, random(5));
	game_timer = 0; 
	break;
    case 1:
	gameInit(1000, 0);	
	break;
    case 2:
	gameInit(1000, 1);
	break;
    case 3:
	gameInit(1000, 2);
	break;
    case 4:
	gameInit(1000, 3);
	break;
    case 5:
	gameInit(1000, 4);
	break;
    case 6:
	gameInit(20, 0);
	game_timer = 0; 
	break;
    case 7:
	gameInit(50, 0);
	game_timer = 0; 
	break;
    case 8:
	gameInit(100, 0);
	game_timer = 0; 
	break;
    }

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

ICACHE_RAM_ATTR void detectRotation() {
    int dir = rotary->process(); 
    int n = 0, m; 
    change = true; 
    switch (state) { 
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
    switch (state) {
    case STATE_INTRO:
	if (ACTION) {
	    last_button_action = millis(); 
	    setState(STATE_GAME_SELECT);
	    clk = 0; 
	}
	break;
    case STATE_GAME_SELECT:
	if (ACTION) {
	    long seed = millis(); 
	    last_button_action = millis(); 

	    int game_type = encode(encoder_count, 9);
	    if (game_type >= 1 && game_type < 6) { 
		sendWiFiCommand(MESSAGE_START_0 + game_type - 1, seed);
	    }
	    gameStart(game_type, seed);
	    clk = 0; 
	}
	break;
    case STATE_GAME:
	if (ACTION) {
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
	}
	break;
    case STATE_END_GAME:
	if (ACTION) {
	    last_button_action = millis(); 
	    setState(STATE_GAME_SELECT);
	    clk = 0; 
	}
	break;
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
    for (i=0 ; (WiFi.status() != WL_CONNECTED) && i<10 ; ++i) {
	delay(200);
	Serial.print(".");
    }
    if (i < 10) {
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

	WiFi.softAP(ssid, password);
	serverIP = WiFi.softAPIP();
	Serial.print("AP IP address: ");
	Serial.println(serverIP);

	// Begin listening on UDP port
	udp.begin(port);
	Serial.printf("Listening on UDP port %d\n", port);
    }
}

void startIncoming() {
    switch(incoming.message) {
    case MESSAGE_START_0:
	gameStart(1, incoming.seed);
	break;
    case MESSAGE_START_1:
	gameStart(2, incoming.seed);
	break;
    case MESSAGE_START_2:
	gameStart(3, incoming.seed);
	break;
    case MESSAGE_START_3:
	gameStart(4, incoming.seed);
	break;
    case MESSAGE_START_4:
	gameStart(5, incoming.seed);
	break;
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
	Serial.printf("server received packet: %d %ld\n", incoming.message, incoming.seed);
	// Store client IP and port from the packet metadata
	clientIP = udp.remoteIP();

	if (state == STATE_GAME_SELECT) {
	    startIncoming(); 
	}
    }
    if (client) {
	Serial.printf("client received packet: %d %ld\n", incoming.message, incoming.seed);

	if (state == STATE_GAME_SELECT) {
	    startIncoming(); 
	}
    }

}

void sendWiFiCommand(int message, long seed) {
    incoming.message = message;
    incoming.seed = seed;

    if (client) { 
	Serial.printf("client sending packet: %d %ld\n", message, seed);
	udp.beginPacket(serverIP, port);
    } else {
	Serial.printf("server sending packet: %d %ld\n", message, seed);
	udp.beginPacket(clientIP, port);	
    }
    udp.write((char*)&incoming, sizeof(incoming));
    udp.endPacket(); 
}

void loop() {
    detectPush();
    listenWiFiCommand();

    switch(state) {
    case STATE_INTRO:
	drawFrameIntro(display);
	if (clk > 100) {
	    setState(STATE_GAME_SELECT);
	} else {
	    break;
	}
    case STATE_GAME_SELECT:
	if (change) {
	    drawFrameSelect(display);
	}
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

    display.display();
    clk++;
    delay(20);
}

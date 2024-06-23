#include "ESP8266WiFi.h"
#include <SSD1306Wire.h>
#include <Wire.h>
#include <SoftWire.h>
#include <stdlib.h>

char dbg_str[256];

#define D9 3
#define MPU 0x68

SSD1306Wire display(0x3c, D1, D2);//, GEOMETRY_128_64, I2C_ONE, 100000);
SoftWire i2c(D3, D9);

#define W 128
#define H 64

int spillage = 0;
int fillage = 0; 
int backage = 0; 

const int nums[] = {1,2,3};
const int count = sizeof(nums) / sizeof(int);

#include "sprites.h"



//SPRITE_EMPTY1 -> index 0
//SPRITE_EMPTY2 -> index 1
#define EMPTY_IDX(x) (-(x) - 1)

#define IS_EMPTY(x) ((x) < 0)

const int nsprite = sizeof(sprite) / sizeof(sprite[0]);


#define MAX_INGR 10

typedef struct {
    int outcome; 
    int ingr[MAX_INGR];
} rule_t; 


#include "rules.h"

/* const rule_t ruleset[] = { */
/*     {SPRITE_OVEN, {1, SPRITE_SQUARE, 1, SPRITE_TRI}}, */
/*     {SPRITE_PLANT, {1, SPRITE_SQUARE, 1, SPRITE_CIRCLE}}, */
/*     {SPRITE_BREAD, {1, SPRITE_PLANT, 1, SPRITE_OVEN}}, */
/* }; */

const int nrule = sizeof(ruleset) / sizeof(rule_t);

typedef struct {
    int sprite_id;
    float x, y, vx, vy;
    float vx0, vy0; 
    int w, h; 
} crit_t;

typedef struct {
    int crit_count[nsprite];
} borcan_t;

#define EMPTY_COUNT 2

borcan_t empties[EMPTY_COUNT];

#define MAX_CRIT 15

crit_t crit[MAX_CRIT];
int ncrit = 0;
long tick = 0; 

char i2cRxBuf[16];
char i2cTxBuf[16];

/*
  pin lore
d9 as 3 for GPIO3 is true
d8 works as a digital input but doesn't seem to pullup - it reads zero as default and 1 when connected to 3.3v
a0 works as analog input  

d3 is the same d3 from the joystick right switch

weirdly the joystick left resets 

*/

void drawSprite(int sprite_id, int x, int y) {
    const uint8_t *sp = sprite[sprite_id];

    if (!sp) {
	return;
    }
    int sp_x = 0;
    int sp_y = 0;
    const int sp_w = (int)sp[0];
    const int sp_h = (int)sp[1];
    int sp_xend = sp_w;
    int sp_yend = sp_h;

    int xend = x + sp_w;
    int yend = y + sp_h;

    if (x < 0) {
	sp_x -= x;
    }
    if (y < 0) {
	sp_y -= y;
    }
    if(xend > W) {
	sp_xend -= (xend - W);
    }
    if(yend > H) {
	sp_xend -= (xend - W);
    }
    for (int i=sp_x ; i<sp_xend ; ++i) {
	for (int j=sp_y ; j<sp_yend ; ++j) {
	    uint8_t val = sp[2 + i + j * sp_w];
	    if (val < 2) {
		display.setPixelColor(i + x, j + y, val == 1 ? WHITE : BLACK);
	    }
	}
    }
}


float wfloat() {
  int16_t i16 = i2c.read() << 8 | i2c.read();
  return  i16 / 16384.0f;
}

void doMPU(char* s) {
    char s2[100];
    if (!s) {
	s = s2;
    }

    i2c.beginTransmission(MPU);
    i2c.write(0x3B);
    i2c.endTransmission(0);
    i2c.requestFrom(MPU, 6); 

    float y=wfloat(), x=wfloat(), z=wfloat();

    for (int i=0 ; i<ncrit ; ++i) {
	crit[i].vx = (crit[i].vx - x * 0.1) * 0.98;
	crit[i].vy = (crit[i].vy + y * 0.1) * 0.98;

	crit[i].x += crit[i].vx + crit[i].vx0;
	crit[i].y += crit[i].vy + crit[i].vy0;
	
	if (crit[i].x < 0) {
	    crit[i].x = 0; 
	    crit[i].vx = fabs(crit[i].vx);
	    crit[i].vx0 = fabs(crit[i].vx0);
	}
	if (crit[i].y < 0) {
	    crit[i].y = 0; 
	    crit[i].vy = fabs(crit[i].vy);
	    crit[i].vy0 = fabs(crit[i].vy0);
	}
	if (crit[i].x + crit[i].w > W) {
	    crit[i].x = W - crit[i].w; 
	    crit[i].vx = -fabs(crit[i].vx);
	    crit[i].vx0 = -fabs(crit[i].vx0);
	}
	if (crit[i].y + crit[i].h > H) {
	    crit[i].y = H - crit[i].h; 
	    crit[i].vy = -fabs(crit[i].vy);
	    crit[i].vy0 = -fabs(crit[i].vy0);
	}
    }


    /* sprintf(s, "empty1: square %d circle %d tri %d oven %d",  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY1)].crit_count[SPRITE_SQUARE],  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY1)].crit_count[SPRITE_CIRCLE],  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY1)].crit_count[SPRITE_TRI], */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY1)].crit_count[SPRITE_OVEN]); */

    /* sprintf(s, "empty2: square %d circle %d tri %d oven %d",  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY2)].crit_count[SPRITE_SQUARE],  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY2)].crit_count[SPRITE_CIRCLE],  */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY2)].crit_count[SPRITE_TRI], */
    /* 	    (int)empties[EMPTY_IDX(SPRITE_EMPTY2)].crit_count[SPRITE_OVEN]); */
    /* Serial.println(s); */

    s[0] = 0;
    spillage = fillage = backage = 0;
    if (z > 0.0) {
	sprintf(s, "spill");
	spillage = 1;
    }
    if (z < 0.5) {
	if (x < -0.3) {
	    sprintf(s, "back");	   
	    backage = 1; 
	} else {
	    sprintf(s, "fill");
	    fillage = 1;
	}
    }
    /* Serial.println(s); */
}

void setup() {
    Serial.begin(9600);
    while (!Serial) {
	delay(10);
    }
    delay(200);
    Serial.println("I AM SUPER CERIALLY");
    delay(200);

    i2c.setTxBuffer(i2cTxBuf, sizeof(i2cTxBuf));
    i2c.setRxBuffer(i2cRxBuf, sizeof(i2cRxBuf));
    i2c.setDelay_us(5);
    i2c.setTimeout(500);
    i2c.begin();
    delay(300);

    i2c.beginTransmission(MPU);
    i2c.write(0x6B);
    i2c.write(0x00);
    i2c.endTransmission();

    i2c.beginTransmission(MPU);
    i2c.write(0x1C);
    i2c.write(0x0);
    i2c.endTransmission();

    delay(200);
    doMPU(NULL);


    /* pinMode(D4,OUTPUT); // onboard led */
    /* for (int i=0 ; i<4 ; ++i) { */
    /* 	digitalWrite(D4,LOW); // onboard led on */
    /* 	delay(100); // wait 1 second */
    /* 	digitalWrite(D4,HIGH); // onboard led off */
    /* 	delay(100); // wait 1 second */
    /* } */
    /* pinMode(A0, INPUT); */

    /* pinMode(D4, INPUT_PULLUP); */
    /* pinMode(D8, INPUT_PULLUP); */
    /* pinMode(D9,INPUT_PULLUP); */
    /* pinMode(D3,INPUT_PULLUP); // right switch */
    pinMode(D5,INPUT_PULLUP); // enter switch
    /* pinMode(D6,INPUT_PULLUP); // down switch */
    /* pinMode(D7,INPUT_PULLUP); // up switch */

    display.init(); // initialize oled
    display.setFont(ArialMT_Plain_10);
    display.clear(); // clear oled buffer
    display.drawString(0,0,"Demo Starting");
    display.display(); // display oled buffer

    delay(300); // wait 3 seconds
}

int myRand(int start, int stop) {
    if (start == stop) {
	return start;
    }
    if (start > stop) {
	start ^= stop;
	stop ^= start;
	start ^= stop; 
    }
    return start + (rand() % (stop - start + 1));
}

void genCrit(int sprite_id) {
    if (ncrit >= MAX_CRIT) {
	return;
    }

    if (IS_EMPTY(sprite_id)) {
	int idx = EMPTY_IDX(sprite_id);
	if (idx < 0 || idx >= EMPTY_COUNT) {
	    return;
	}
	for (int i=nsprite-1 ; i>=0 ; --i) {
	    if (empties[idx].crit_count[i] > 0) {
		empties[idx].crit_count[i]--;
		sprite_id = i;
		break;
	    }
	}
    }

    if (IS_EMPTY(sprite_id)) { // the empty is empty
	return;
    }

    crit[ncrit].w = sprite[sprite_id][0];
    crit[ncrit].h = sprite[sprite_id][1];
    crit[ncrit].x = myRand(80, W - crit[ncrit].w);
    crit[ncrit].y = myRand(0, H - crit[ncrit].h);

    crit[ncrit].vx = 0; 
    crit[ncrit].vy = 0; 
    crit[ncrit].vx0 = myRand(-60, 60) * 0.01; 
    crit[ncrit].vy0 = myRand(-60, 60) * 0.01;

    crit[ncrit].sprite_id = sprite_id;
    
    ncrit++;
}

#define EMPTY_CYCLE 1500

void updateEmpties() {
    borcan_t* bork;
    static unsigned long last_update = 0;
    
    unsigned long now = millis();
    if (!last_update) {
	last_update = now;
	return;
    }

    if (now - last_update < EMPTY_CYCLE) {
	return; 
    }
    last_update = now;

    /* if (dbg_str[0] == 0) { */
    /* 	sprintf(dbg_str, "%d %d %d %d %d", ruleset[0].outcome,  */
    /* 		ruleset[0].ingr[0], ruleset[0].ingr[1], ruleset[0].ingr[2], ruleset[0].ingr[3]); */
    /* }; */

    for (int i=0 ; i<EMPTY_COUNT ; ++i) {
	bork = empties + i;
	for (int r=0 ; r<nrule ; ++r) {
	    int ok = 1; 
	    for (int j=0 ; j<MAX_INGR ; j+=2) {
		int count_raw = (int)ruleset[r].ingr[j]; // the countity required
		int count = abs(count_raw);
		int ingr = ruleset[r].ingr[j+1]; // the ingredient required

		if(!count) {
		    break;
		}
		if (bork->crit_count[ingr] < count) { 
		    ok = 0;
		    break;
		}
	    }
	    if (ok) {
		dbg_str[0] = 0;
		for (int j=0 ; j<MAX_INGR ; j+=2) {
		    int count_raw = ruleset[r].ingr[j];
		    int count = abs(count_raw);
		    int ingr = ruleset[r].ingr[j+1];
		    if(!count) {
			break;
		    }
		    if (count_raw < 0) {
			bork->crit_count[ingr] -= count;
//			sprintf(dbg_str + strlen(dbg_str), "ate%d", ingr);
		    }
		}
		int outcome = ruleset[r].outcome;
		if (outcome != SPRITE_NONE) {
		    bork->crit_count[outcome]++;
//		    sprintf(dbg_str + strlen(dbg_str), "made%d", outcome);
		}
		break; // one rule activation only per empties update per borcan
	    }
	}
    }
}

void tryBackage(int sp_id) {
    for (int i=0 ; i<ncrit ; ++i) {
	int crit_sp_id = crit[i].sprite_id;
	int x = (int)sprite[crit_sp_id][0] + (int)crit[i].x;
	if ((sp_id == crit_sp_id || sp_id < 0) && x >= W - 3) {
	    for ( ; i<ncrit-1 ; ++i) {
		crit[i] = crit[i + 1];
	    }
	    if (sp_id < 0) { // filling an empty
		int idx = EMPTY_IDX(sp_id);
		if (idx >= 0 && idx < EMPTY_COUNT) {
		    empties[idx].crit_count[crit_sp_id]++;
		}
	    }
	    ncrit--;
	    return;
	}
    }
}

void loop() {
    static int blink = 0; 
    char s[100];

    int d5 = digitalRead(D5);
    int d6 = digitalRead(D6);
    int d7 = digitalRead(D7);

    int a0 = analogRead(A0);

    int borcan = 0; 

    tick++;
    doMPU(s);

    updateEmpties();

    display.clear(); // clear oled buffer
    if (dbg_str[0]) {
	dbg_str[20] = 0; 
	display.drawString(0,0, dbg_str);
    }
    //display.drawString(0,13,"enter switch:"+String(d5));
    //display.drawString(0,26,"down switch:"+String(d6)+ "up switch:"+String(d7));

    display.drawString(0,39,s + String(a0));

    borcan = SPRITE_NONE;
    if (a0 > 665 && a0 < 795) {
	borcan = SPRITE_CIRCLE; 
    }
    if (a0 > 40 && a0 < 100) {
	borcan = SPRITE_SQUARE; 
    }

    if (a0 > 450 && a0 < 630) {
	borcan = SPRITE_EMPTY1; 
    }
    if (a0 > 120 && a0 < 250) {
	borcan = SPRITE_EMPTY2; 
    }
    if (a0 > 830 && a0 < 950) {
	borcan = SPRITE_TRI; 
    }

    if (borcan != SPRITE_NONE) {
	display.drawRect(0,0,128,64);
    }

    //display.drawString(0,52,s);

    ++blink;

    if (backage && blink > 5) {
	blink = 0; 
	tryBackage (borcan);
    }

    if (blink > 20) {
	blink = 0; 
	if ((borcan > 0 || IS_EMPTY(borcan)) && fillage && ncrit < MAX_CRIT) {
	    genCrit(borcan);
	}
	if (spillage && ncrit > 0) {
	    ncrit--;
	    for (int i=0 ; i<ncrit ; ++i) {
		crit[i] = crit[i + 1];
	    }
	}
    }
    for (int i=0 ; i<ncrit ; ++i) {
	drawSprite(crit[i].sprite_id, crit[i].x, crit[i].y);
    }

    display.display(); // display oled buffer
    delay(20); // wait for 100 milliseconds
}

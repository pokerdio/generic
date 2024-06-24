#include "ESP8266WiFi.h"
#include <SSD1306Wire.h>
#include <Wire.h>
#include <SoftWire.h>

#define D9 3
#define MPU 0x68

SSD1306Wire display(0x3c, D1, D2);//, GEOMETRY_128_64, I2C_ONE, 100000);
SoftWire i2c(D3, D9);

const int nums[] = {1,2,3};
const int count = sizeof(nums) / sizeof(int);


const uint8_t sprite[] = {11, 9, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 
1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 
1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 
1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 
1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 
1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 
1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
};

const uint8_t* sprites[] = {sprite};

const int nsprites = sizeof(sprites) / sizeof(sprites[0]);

typedef struct {
    uint8_t type;
    uint8_t sprite_id;
} crits;

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

    float x=wfloat(), y=wfloat(), z=wfloat();
    sprintf(s, "xyz: %.2f %.2f %.2f", x, y, z);

    Serial.println(s);
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

void loop() {
    static int blink = 0; 
    char s[100];

    int d5 = digitalRead(D5);
    int d6 = digitalRead(D6);
    int d7 = digitalRead(D7);

    int a0 = analogRead(A0);

    doMPU(s);

    display.clear(); // clear oled buffer
    display.drawString(0,0,"Demo Running "+String(D1==SCL)+" "+String(D2==SDA));
    display.drawString(0,13,"enter switch:"+String(d5));
    display.drawString(0,26,"down switch:"+String(d6)+ "up switch:"+String(d7));
    display.drawString(0,39,"a0" + String(a0));
    display.drawString(0,52,s);

    blink = !blink;
    if (blink) {
	for (int i=125 ; i<128 ; ++i) {
	    for (int j = 0 ; j<7 ; ++j) {
		display.setPixel(i, j);
	    }
	}
    }

    if (!d5) {
	for (int i=63 ; i<128 ; ++i) {
	    for (int j=0 ; j<64 ; ++j) {
		display.setPixelColor(i, j, ((i * j) / 8) % 2 ? BLACK : WHITE);
	    }
	}
    }
    display.display(); // display oled buffer
    delay(1000); // wait for 100 milliseconds
}

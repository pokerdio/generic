//esp8266 nodemcu version


#include <Arduino.h>
#include <Wire.h>
#include <U8g2lib.h>
#include <Servo.h>

Servo servo;

#define MPU 0x68

//U8G2_SSD1306_128X32_UNIVISION_F_SW_I2C u8g2(U8G2_R0, /* clock=*/ 21, /* data=*/ 20, /* reset=*/ U8X8_PIN_NONE);   // Adafruit Feather M0 Basic Proto + FeatherWing OLED
//U8G2_SSD1306_128X32_UNIVISION_F_SW_I2C u8g2(U8G2_R2, /* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE);   // Adafruit Feather ESP8266/32u4 Boards + FeatherWing OLED
//U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R0, /* reset=*/ U8X8_PIN_NONE);  // Adafruit ESP8266/32u4/ARM Boards + FeatherWing OLED
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R2, /* reset=*/ U8X8_PIN_NONE, /* clock=*/ SCL, /* data=*/ SDA);   // pin remapping with ESP8266 HW I2C



void setup() {
  // put your setup code here, to run once:

  servo.attach(D0);
  
  Wire.begin();
  Wire.beginTransmission(MPU);
  Wire.write(0x6B);
  Wire.write(0x00);
  Wire.endTransmission();

  Wire.beginTransmission(MPU);
  Wire.write(0x1C);
  Wire.write(0x0);
  Wire.endTransmission();

  u8g2.begin();
  
  Serial.begin(9600);
  while (!Serial) {
    delay(10);
  }
}


float wfloat() {
  int16_t i16 = Wire.read() << 8 | Wire.read();
  return  i16 / 16384.0f;
}
void loop() {
  // put your main code here, to run repeatedly:
  char s[100];

  Wire.beginTransmission(MPU);
  Wire.write(0x3B);
  Wire.endTransmission(0);
  Wire.requestFrom(MPU, 6, 1); 

  float x=wfloat(), y=wfloat(), z=wfloat();
  sprintf(s, "xyz : %.2f %.2f %.2f", x, y, z);
  Serial.println(s);
  
  u8g2.clearBuffer();          // clear the internal memory
  u8g2.setFont(u8g2_font_ncenB08_tr); // choose a suitable font
  u8g2.drawStr(0,10, s);  // write something to the internal memory
  u8g2.sendBuffer();          // transfer internal memory to the display


  servo.write(80 + x * 90);
  delay(100);
}

// bits borrowed from  https://github.com/slu4coder/ArduinoPS2Keyboard

// Lookup table (in: SHIFT state and PS2 scancode => out: desired ASCII code) change for your country
// QWERTY layout
char ScancodeToASCII[2][128] = {
    { 0, 0, 0, 0, 0, 27, 27, 0,         
      0, 0, 0, 0, 0, 9, 96, 0,         
      0, 0, 0, 0, 0, 113, 49, 0,       
      0, 0, 122, 115, 97, 119, 50, 0, // w/o SHIFT or ALT(GR)
      0, 99, 120, 100, 101, 52, 51, 0, 
      0, 32, 118, 102, 116, 114, 53, 0, 
      0, 110, 98, 104, 103, 121, 54, 0, 
      0, 0, 109, 106, 117, 55, 56, 0,

      0, 44, 107, 105, 111, 48, 57, 0, 0, 
      46, 47, 108, 59, 112, 45, 0,  
      0, 0, 39, 0, 91, 61, 0, 0,     
      0, 0, 10, 93, 0, 124, 0, 0,
      0, 60, 0, 0, 0, 0, 8, 0,        
      0, 49, 0, 52, 55, 0, 0, 0,          
      0, 46, 50, 53, 54, 56, 27, 0,  
      0, 43, 51, 45, 42, 57, 0, 0   },
    { 0, 0, 0, 0, 0, 0, 0, 0,         
      0, 0, 0, 0, 0, 0, 126, 0,        
      0, 0, 0, 0, 0, 81, 33, 0,        
      0, 0, 90, 83, 65, 87, 64, 35, // with SHIFT
      0, 67, 88, 68, 69, 36, 35, 0,    
      0, 32, 86, 70, 84, 82, 37, 0,     
      0, 78, 66, 72, 71, 89, 94, 0,    
      0, 0, 77, 74, 85, 38, 42, 0,
      0, 60, 75, 73, 79, 41, 40, 0,   
      0, 62, 63, 76, 58, 80, 95, 0,   
      0, 0, 34, 0, 123, 43, 0, 0,      
      0, 0, 0, 125, 0, 92, 0, 0,
      0, 62, 0, 0, 0, 0, 0, 0,        
      0, 0, 0, 0, 0, 0, 0, 0,          
      0, 0, 0, 0, 0, 0, 0, 0,          
      0, 0, 0, 0, 0, 0, 0, 0  }
};

int kbd_bit = 0;
int kbd_value = 0;
int kbd_activity = 0;
int kbd_parity = 0;
#include <Wire.h>
#include <U8g2lib.h>
#include <stdio.h>
#include <stdlib.h>
U8G2_SSD1306_128X32_UNIVISION_F_HW_I2C u8g2(U8G2_R2, /* reset=*/ U8X8_PIN_NONE, /* clock=*/ PC5, /* data=*/ PC4);   // pin remapping with ESP8266 HW I2C

#define MAXMSG 14
char msg[MAXMSG + 5] = "";


void draw() {
  u8g2.clearBuffer();          // clear the internal memory
 
  u8g2.drawStr(0, 16, msg); // write something to the internal memory
  u8g2.sendBuffer();          // transfer internal memory to the display
}

void randInit(void) {
  int i, seed; 
  for (i=0 ; i<240 ; ++i) {
    seed += analogRead(PC0);
  }
  srand(seed);
}
void setup() {
  pinMode(PC0, INPUT_PULLUP);
  Serial.begin(9600);
  randInit(); 
  u8g2.begin();
  u8g2.setFont(u8g2_font_7x14_tf); // choose a suitable font
  

  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  draw();
  //establishContact();  // send a byte to establish contact until receiver responds


  noInterrupts();
  // PCICR means PCI control register
  //PCICR = 0b00000001; //enable port b for interrupts
  //PCICR = 0b00000010; //enable port c for interrupts
  PCICR = 0b00000100; //enable port d for interrupts
  PCMSK2 = 0b01000000; //enable pin D6  (PCMSK2 for D register)
  DDRD = 0; // all inputs
  interrupts();
}

void loop() {
  // if we get a valid byte, read analog ins:
  if (Serial.available() > 0) {
    // get incoming byte:
    String str = Serial.readString();
    str.trim();
    str = "---===" + str + "===---\n";
    Serial.println(str);
  }
  draw();
  delay(50); // if mid 11 bit block, give until next loop for interrupt to finish
  // if during that time interrupt isn't active, reset the bit count.
  if (!kbd_activity) {
    kbd_bit = 0;
    kbd_value = 0;
  }
  kbd_activity = 0;
}

void establishContact() {
  int i = 0;
  while (Serial.available() <= 0) {
    Serial.print("A");   // send a capital A
    delay(300);
  }
}
/*ISR(PCINT0_vct) {...} //ISR for PCINT0 to PCINT7
  ISR(PCINT1_vct) {...} //ISR for PCINT8 to PCINT15
  ISR(PCINT2_vct) {...} //ISR for PCINT16 to PCINT23
*/
ISR(PCINT2_vect) {
  kbd_activity = 1;
  static bool shift = false;
  static bool nextRelease = false;

  if (!bitRead(PIND, 6)) {
    return;
  }
  int p5 = bitRead(PIND, 5);
  if (kbd_bit >= 1 && kbd_bit <= 8) {
    kbd_value |= p5 << (kbd_bit - 1);
  }

  kbd_parity ^= p5;
  if (++kbd_bit < 11) {
    return;
  }
  //  Serial.print(kbd_value);
  //  Serial.println(kbd_parity ? " ERR" : " OK");

  switch (kbd_value) {
    case 18:
    case 89:
      shift = !nextRelease;
      nextRelease = false;
      break;
    case 240:
      nextRelease = true;
      break;
    default:
      if (!nextRelease) {
        int key = ScancodeToASCII[shift][kbd_value & 127];
        if (key == 8) {
          if (msg[0]) {
            msg[strlen(msg) - 1] = 0;
          }
        } else if (strlen(msg) < MAXMSG && key != '\n') {
          msg[strlen(msg) + 1] = 0;
          msg[strlen(msg)] = key;
        } else {
          msg[0] = 0;
        }
        Serial.println((int)key);
      }
      nextRelease = false;
      break;
  }
  kbd_value = 0;
  kbd_activity = 0;
  kbd_bit = 0;
  kbd_parity = 0;
}

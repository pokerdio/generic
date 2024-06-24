#include <avr/io.h>

#define LED 3

void writePin(uint8_t pin, uint8_t val) {
  if (val) {
    PORTA.OUT |= 1 << pin;    
  } else {
    PORTA.OUT &= ~(1<< pin);
  }
}

void setup() {
  // put your setup code here, to run once:
//  PORTA.DIR &= ~(1 << INPIN);
  PORTA.DIR |= (1 << LED);
 
}

void loop() {
  writePin(LED, 1);
  delay(50);
  writePin(LED, 0);
  delay(200);
  writePin(LED, 1);
  delay(50);
  writePin(LED, 0);
  delay(200);
  writePin(LED, 1);
  delay(50);
  writePin(LED, 0);
  delay(3250);
  
}

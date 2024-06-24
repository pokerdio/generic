/*
  ESP8266 Blink by Simon Peter
  Blink the blue LED on the ESP-01 module
  This example code is in the public domain

  The blue LED on the ESP-01 module is connected to GPIO1
  (which is also the TXD pin; so we cannot use Serial.print() at the same time)

  Note that this sketch uses LED_BUILTIN to find the pin with the internal LED
*/

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  
}

void led(bool lit, int delay_time) {
  digitalWrite(LED_BUILTIN, lit ? LOW : HIGH);
  delay(delay_time);
}

// the loop function runs over and over again forever
void loop() {
  led(false, 1500);
  led(true, 5);
  led(false,70);
  led(true, 5);
}

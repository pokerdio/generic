//This example code is in the Public Domain (or CC0 licensed, at your option.)
//By Evandro Copercini - 2018
//
//This example creates a bridge between Serial and Classical Bluetooth (SPP)
//and also demonstrate that SerialBT have the same functionalities of a normal Serial



void setup() {
  Serial.begin(115200);
  Serial.println("Hello world!");
}

void loop() {
  while (Serial.available()) {
    Serial.write(Serial.read());
  }
  delay(20);
}

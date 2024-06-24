#include <ESP8266WiFi.h>        // Include the Wi-Fi library

const char* ssid     = "esp8266";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "rodoid";     // The password of the Wi-Fi network

void setup() {
    Serial.begin(9600);         // Start the Serial communication to send messages to the computer
    delay(10);
    Serial.println('\n');
  

    WiFi.softAP(ssid, password);             // Connect to the network
    Serial.print("access point ");
    Serial.print(ssid);
    Serial.println(" started");
    Serial.print("AP ip address: ");
    Serial.println(WiFi.softAPIP());

}

void loop() {
}

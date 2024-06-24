#include <ESP8266WiFi.h>
 
void setup()
{
    Serial.begin(115200);
    WiFi.mode(WIFI_STA);
    pinMode(2, OUTPUT);
}

int x;  
void loop() 
{
    Serial.println(WiFi.macAddress());
    delay(1000);
    x = !x; 
    digitalWrite(2, x);
}

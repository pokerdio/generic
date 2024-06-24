#include <ESP8266WiFi.h>
#include <espnow.h>

#define SMOL
// REPLACE WITH THE MAC Address of your receiver 

#ifdef SMOL
int x = 200; 
uint8_t peer_address[] = {0x5C, 0xCF, 0x7F, 0x8B, 0x13, 0xA0};//peer is big square aux chip
#else
uint8_t peer_address[] = {0x2C, 0xF4, 0x32, 0x8B, 0xAB, 0xBE};//peer is smol rectangle aux chip
int x = 25000;
#endif

int y = 0;


// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
    Serial.print("Last Packet Send Status: ");
    if (sendStatus == 0){
        Serial.println("Delivery success");
    }
    else{
        Serial.println("Delivery fail");
    }
}

// Callback when data is received
void OnDataRecv(uint8_t * mac, uint8_t *incomingData, uint8_t len) {
    Serial.print("Bytes received: ");
    Serial.print(len);
    if (len <= 0) {
        return;
    }
    for (int i=0 ; i<len-1 ; ++i) {
        Serial.print(" ");
        Serial.print(incomingData[i]);
    }
    Serial.println(incomingData[len - 1]);
}

void setup() {
    // Init Serial Monitor
    Serial.begin(115200);

    // Set device as a Wi-Fi Station
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();

    // Init ESP-NOW
    if (esp_now_init() != 0) {
        Serial.println("Error initializing ESP-NOW");
        return;
    }

    // Set ESP-NOW Role
    esp_now_set_self_role(ESP_NOW_ROLE_COMBO);

    // Once ESPNow is successfully Init, we will register for Send CB to
    // get the status of Trasnmitted packet
    esp_now_register_send_cb(OnDataSent);
  
    // Register peer
    esp_now_add_peer(peer_address, ESP_NOW_ROLE_COMBO, 1, NULL, 0);
  
    // Register for a callback function that will be called when data is received
    esp_now_register_recv_cb(OnDataRecv);

    pinMode(2, OUTPUT);
}
 

void loop() {
    // Send message via ESP-NOW
    ++x;
    esp_now_send(peer_address, (uint8_t *) &x, sizeof(x));

    digitalWrite(2, 0);
    delay(50);
    digitalWrite(2, 1);
    delay(500);
}

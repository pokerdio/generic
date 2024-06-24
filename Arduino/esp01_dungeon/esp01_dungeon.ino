#include <ESP8266WiFi.h>
#include <espnow.h>

#define SMOL

#ifdef SMOL
uint8_t peer_address[] = {0x5C, 0xCF, 0x7F, 0x8B, 0x13, 0xA0};//peer is big square aux chip
#else
uint8_t peer_address[] = {0x2C, 0xF4, 0x32, 0x8B, 0xAB, 0xBE};//peer is smol rectangle aux chip
#endif

typedef struct {
    uint8_t x;
    uint8_t y;
} xy_t; 

#define MAP_SIZE 8

int x = 1, y = 1; 
int x2 = MAP_SIZE+1, y2 = MAP_SIZE+1; 

int but[4] = {0,0,0,0};

#define SEND_TICKS 25
int send_cd = SEND_TICKS;

#define BLINK_LIT_TICKS 10
#define BLINK_CYCLE 20
int blink_cd = 0; 



byte v[MAP_SIZE][MAP_SIZE] = {
    {1,1,1,1,1,1,1,1},
    {1,0,0,0,0,0,0,1},
    {1,0,1,1,1,1,1,1},
    {1,0,1,0,0,0,1,1},
    {1,0,1,0,1,0,1,1},
    {1,0,1,0,1,1,1,1},
    {1,0,0,0,0,0,0,1},
    {1,1,1,1,1,1,1,1},
};


// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
}

// Callback when data is received
void OnDataRecv(uint8_t * mac, uint8_t *incomingData, uint8_t len) {
    if (len >= 2) {
        x2 = (int)incomingData[0];
        y2 = (int)incomingData[1];
    }
}


void w(int pin, int val) {
    digitalWrite(pin, val);
}



void setup() {
    // put your setup code here, to run once:
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);  
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);  
    for (int i=0 ; i<4 ; ++i) {
        w(i, LOW);
    }



    // Set device as a Wi-Fi Station
    WiFi.mode(WIFI_STA);
    WiFi.disconnect();

    // Init ESP-NOW
    if (esp_now_init() != 0) {
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


}

void adjust_xy(int & val) {
    if (val < 1) {
        val = 1; 
    }
    if (val > MAP_SIZE - 2) {
        val = MAP_SIZE - 2; 
    }
}

void adjust_all(void) {
    adjust_xy(x);
    adjust_xy(y);
    adjust_xy(x2);
    adjust_xy(y2);
}

int readButPress(int a, int b) {
    for (int i=0 ; i<4 ; ++i) {
        if (i == a) {
            pinMode(i, OUTPUT);
            w(i, LOW);
        } else {
            if (i) {
                pinMode(i, INPUT_PULLUP);
            } else {
                pinMode(i, INPUT); // GPIO0 is already pulled up by default.
            }
        }
    }
    volatile int ret = 0; 
    for (int i=0 ; i<25 ; ++i) {
        ret += 5;
    }
    ret = !digitalRead(b);
    pinMode(a, INPUT_PULLUP);
    return ret;
}

int blink[4] = {0,0,0,0};

void blinkAll (int k) {
    if (k >= 0 && k < 4) {
        if (blink[k]) {
            return;
        }
        blink[k] = 1; 
    }
    for (int j=0 ; j< 3 + k * 2 ; ++j) {
        for (int i=0 ; i<4 ; ++i) {
            pinMode(i, OUTPUT);
            w(i, HIGH);
        }
        delay(100);
        for (int i=0 ; i<4 ; ++i) {
            pinMode(i, INPUT);
        }
        delay(300);
    }
    delay(1000);
}

void litPin(int x, int y, int pin) {
    if (v[y][x]) { 
        pinMode(pin, INPUT);
    } else {
        if (x == x2 && y == y2 && blink_cd >= BLINK_LIT_TICKS) {
            pinMode(pin, INPUT);
            return;
        }
        pinMode(pin, OUTPUT);
        w(pin, HIGH);
    }
}

void loop() {
    // put your main code here, to run repeatedly:
    adjust_all();

    //up
    if (readButPress(0, 3)) {
        //blinkAll(0);
        but[0] = 1; 
    } else if (but[0] == 1)  {
        but[0] = 0; 
        if (v[y - 1][x] == 0) {
            y = y - 1; 
        }
    }

    //down
    if (readButPress(1, 2)) {
        //blinkAll(1);
        but[1] = 1; 
    } else if (but[1] == 1)  {
        but[1] = 0; 
        if (v[y + 1][x] == 0) {
            y = y + 1; 
        }
    }

    //left
    if (readButPress(2, 0)) {
        //blinkAll(2);
        but[2] = 1; 
    } else if (but[2] == 1)  {
        but[2] = 0; 
        if (v[y][x - 1] == 0) {
            x = x - 1; 
        }
    }

    //right
    if (readButPress(3, 1)) {
        //blinkAll(3);
        but[3] = 1; 
    } else if (but[3] == 1)  {
        but[3] = 0; 
        if (v[y][x + 1] == 0) {
            x = x + 1; 
        }
    }

    if (++blink_cd >= BLINK_CYCLE) {
        blink_cd = 0; 
    }


    litPin(x, y - 1, 3);//up
    litPin(x, y + 1, 2);//down
    litPin(x - 1, y, 0);//left
    litPin(x + 1, y, 1);//right

    if (--send_cd < 0) {
        send_cd = SEND_TICKS;
        xy_t xy;
        xy.x = (uint8_t)x;
        xy.y = (uint8_t)y;
        esp_now_send(peer_address, (uint8_t *) &xy, sizeof(xy_t));
    }
    delay(20);
}

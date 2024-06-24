#include <ESP8266WiFi.h>
#include <espnow.h>


void w(int pin, int val) {
    digitalWrite(pin, val);
}


int x = 1, y = 1; 
int x2 = 1, y2 = 1; 

int but[4] = {0,0,0,0};

#define MAP_SIZE 8

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

void setup() {
    // put your setup code here, to run once:
    pinMode(0, OUTPUT);
    pinMode(1, OUTPUT);  
    pinMode(2, OUTPUT);  
    pinMode(3, OUTPUT);  
    for (int i=0 ; i<4 ; ++i) {
        w(i, LOW);
    }
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

    if (v[y - 1][x]) { //up 
        pinMode(3, INPUT);
    } else {
        pinMode(3, OUTPUT);
        w(3, HIGH);
    }

    if (v[y + 1][x]) { //down
        pinMode(2, INPUT);
    } else {
        pinMode(2, OUTPUT);
        w(2, HIGH);
    }

    if (v[y][x-1]) { //left
        pinMode(0, INPUT);
    } else {
        pinMode(0, OUTPUT);
        w(0, HIGH);
    }

    if (v[y][x+1]) { //right
        pinMode(1, INPUT);
    } else {
        pinMode(1, OUTPUT);
        w(1, HIGH);
    }

    delay(20);
}

#include <avr/io.h>

#define DIN 3
#define CS 2
#define CLK 6
#define INPIN 1

// MAX7219 Control registers
#define DECODE_MODE   9
#define INTENSITY    10
#define SCAN_LIMIT   11
#define SHUTDOWN     12
#define DISPLAY_TEST 15

void sendData(uint8_t address, uint8_t val);
void sendByte(uint8_t val);
void writePin(uint8_t pin, uint8_t val);

//8x8 grid data
uint8_t matrix[8]={0};

uint8_t readMatrix(uint8_t x, uint8_t y) {
    return (matrix[y] & (1 << x)) > 0;
}

void setMatrix(uint8_t x, uint8_t y, uint8_t value) {
    if (value) {
        matrix[y] |= (1 << x);
    } else {
        matrix[y] &= ~(1 << x);
    }
}

void matrixUpload() {
    for (int i=0 ; i<8 ; ++i) {
        sendData(i + 1, matrix[i]);
    }
}


void writePin(uint8_t pin, uint8_t val) {
    if (val) {
        PORTA.OUT |= 1 << pin;    
    } else {
        PORTA.OUT &= ~(1<< pin);
    }
}

uint8_t readPin(uint8_t pin) {
    return (PORTA.IN & (1 << pin)) > 0;
}

void sendByte(uint8_t val) {
    uint8_t i = 128;
    while(i > 0) {
        writePin(CLK, 0);
        writePin(DIN, i & val);
        i >>= 1;
        writePin(CLK, 1);
    }
}


void sendData(uint8_t address, uint8_t val) {
    writePin(CS, 0);
    sendByte(address);
    sendByte(val);
    writePin(CS, 1);
}

//x0/y0 is overwritten; all the segment shifts towards x0/y0
void shiftSegment(uint8_t x0, uint8_t y0, uint8_t x1, uint8_t y1) {
    uint8_t x=x0, y=y0;

    while (x0 != x1 || y0 != y1) {
        if (x0 < x1) {
            x = x0 + 1;
        } else if (x0 > x1) {
            x = x0 - 1;
        }
        if (y0 < y1) {
            y = y0 + 1;
        } else if (y0 > y1) {
            y = y0 - 1;
        }
        setMatrix(x0, y0, readMatrix(x, y));
        x0 = x;
        y0 = y;   
    }
}

void spiralShift() {
    for (int i=0 ; i<4 ; ++i) {
        if (i != 0) {
            shiftSegment(i-1, i, 7-i, i);
        } else {
            shiftSegment(0, 0, 7, 0);
        }
        shiftSegment(7-i, i, 7-i, 7-i);
        shiftSegment(7-i, 7-i, i, 7-i);
        shiftSegment(i, 7-i, i, i+1);  
     
    } 
}

void setup() {
    // put your setup code here, to run once:
    PORTA.DIR &= ~(1 << INPIN);
    PORTA.DIR |= 1 << CS;
    PORTA.DIR |= 1 << CLK;
    PORTA.DIR |= 1 << DIN;

    PORTA.PIN1CTRL |= 8;
  
    sendData(DISPLAY_TEST, 0);
    sendData(INTENSITY, 1);
    sendData(SCAN_LIMIT, 0x0f); // "scan all digits"
    sendData(DECODE_MODE, 0); //bcd mode no ty
    for (int i=1 ; i<=8 ; ++i) {
        sendData(i, 0);
    }

    sendData(SHUTDOWN, 1);
}

void loop() {
    spiralShift();
    setMatrix(3, 4, readPin(INPIN));
    matrixUpload(); 
    delay(50);
}

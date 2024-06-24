#include <EEPROM.h>

#define DIN 3
#define CS 2
#define CLK 1

#define WRITE_PIN_0 4
#define WRITE_PIN_1 5
#define WRITE_PIN_2 6
#define WRITE_PIN_3 7


#define READ_PIN_0 0
#define READ_PIN_1 1
#define READ_PIN_2 2
#define READ_PIN_3 3


// MAX7219 Control registers

#define DECODE_MODE     9
#define INTENSITY    0x0A
#define SCAN_LIMIT   0x0B
#define SHUTDOWN     0x0C
#define DISPLAY_TEST 0x0F

#define COM_FULL 101
#define COM_TOP_RIGHT 102
#define COM_TOP_LEFT 103
#define COM_BOTTOM_RIGHT 104
#define COM_BOTTOM_LEFT 105
#define COM_LEFT 106
#define COM_RIGHT 107
#define COM_UP 108
#define COM_DOWN 109

// getKey states 
#define KEY_BASE 1
#define KEY_WAIT_ZERO 2

#define CLICK_FULL 1
#define CLICK_TOP_LEFT 2
#define CLICK_TOP_RIGHT 3
#define CLICK_BOTTOM_LEFT 4 
#define CLICK_BOTTOM_RIGHT 5


int key_state = KEY_BASE;

int click_state = CLICK_FULL; 
uint16_t keyboard_mask = 0;

void writePin (uint8_t pin, uint8_t val) {
    switch(pin) {
    case DIN:
    case CS:
    case CLK:
    case WRITE_PIN_0:
    case WRITE_PIN_1:
    case WRITE_PIN_2:
    case WRITE_PIN_3:
        if (val) {
            PORTA.OUT |= (1 << pin);
        } else {
            PORTA.OUT &= ~(1 << pin);
        }
        break;
    }
}

void writeAll(uint8_t val) {
    for (int i=0 ; i<4 ; ++i) {
        writePin(WRITE_PIN_0 + i, val);
    }
}

uint8_t readPin (uint8_t pin) {
    switch (pin) {
    case READ_PIN_0:
    case READ_PIN_1:
    case READ_PIN_2:
    case READ_PIN_3:
        return (PORTB.IN & (1 << pin)) > 0;
    }
    return 0;
}

int maskCount(uint16_t m) {
    int ret = 0;
    for (int i=0 ; i<16 ; ++i) {
        if (m & (1 << i)) {
            ret += 1;
        }
    }
    return ret;
}

int firstBit(uint16_t mask) {
    for (int bit=0 ; bit<16 ; ++bit) {
        if (mask & (1 << bit)) {
            return bit; 
        }
    }
    return -1; 
}
/* 1 2 4 8 */
/* 16 32 64 128 */
/* 256 512 1024 2048 */
/* 4096 8192 16384 32768 */

int getCorner(int x, int y) {
    if (x < 2 && y < 2) {
        return 0;
    }
    if (y < 2) {
        return 1;
    }
    if (x < 2) {
        return 2;
    }
    return 3;
}

int getTwoKeyCommand(uint16_t old_mask, uint16_t mask) {
    uint16_t new_mask = mask & ~old_mask;
    if (maskCount(new_mask) != 1 || maskCount(old_mask) != 1) {
        return -1; 
    }
    int k0 = firstBit(old_mask);
    int x0 = k0 & 3, y0 = (k0 & 12) >> 2;
    int c0 = getCorner(x0, y0);

    int k1 = firstBit(new_mask);
    int x1 = k1 & 3, y1 = (k1 & 12) >> 2;
    int c1 = getCorner(x1, y1);
    if (c0 == c1) {
        switch(c0) {
        case 0:
            return COM_TOP_LEFT;
        case 1:
            return COM_TOP_RIGHT;
        case 2:
            return COM_BOTTOM_LEFT;
        case 3:
            return COM_BOTTOM_RIGHT;
        default:
            return -1;
        }
    }
    if ((c0 == 0 && c1 == 3) || (c0 == 1 && c1 == 2) || 
        (c1 == 0 && c0 == 3) || (c1 == 1 && c0 == 2)) {
        return COM_FULL;
    }
    if ((c0 == 0 || c0 == 2) && (c1 == 1 || c1 == 3)) {
        return COM_RIGHT;
    }
    if ((c0 == 1 || c0 == 3) && (c1 == 0 || c1 == 2)) {
        return COM_LEFT;
    }
    if ((c0 == 0 || c0 == 1) && (c1 == 2 || c1 == 3)) {
        return COM_DOWN;
    }
    if ((c0 == 2 || c0 == 3) && (c1 == 0 || c1 == 1)) {
        return COM_UP;
    }
    return -1;
}

int getKey(void) {
    int k = 0;
    int ret = -1; 
    uint16_t old_mask = keyboard_mask;
    writeAll(1);
    for (int i=0 ; i<4 ; ++i) {
        writePin(WRITE_PIN_3 - i, 0);
        for (int j=READ_PIN_0 ; j<=READ_PIN_3 ; ++j) {
            if (keyboard_mask & (1 << k)) {
                ret = k; 
            }

            if (!readPin(j)) {
                keyboard_mask |= (1 << k);
            } else {
                keyboard_mask &= ~(1 << k); 
            }
            ++k;
        }
        writePin(WRITE_PIN_3 - i, 1);
    }

    switch (key_state) {
    case KEY_BASE:
        switch(maskCount(keyboard_mask)) {
        case 0:
            return ret;
        case 1:
            return -1; 
        case 2:
            key_state = KEY_WAIT_ZERO;
            return getTwoKeyCommand(old_mask, keyboard_mask);
        default:
            key_state = KEY_WAIT_ZERO;
            return -1; 
        }
        break;
    case KEY_WAIT_ZERO:
        if (maskCount(keyboard_mask) == 2 && maskCount(old_mask) == 1) {
            return getTwoKeyCommand(old_mask, keyboard_mask);
        }
        if (keyboard_mask == 0) {
            key_state = KEY_BASE;
        }
        return -1; 
    }
    return -1; 
}


void sendByte(uint8_t val) {
    for (int i = 128 ; i > 0 ; i >>= 1) {
        writePin(CLK, 0);
        writePin(DIN, (i & val) ? 1 : 0);
        writePin(CLK, 1);
    }
}

void sendByteRev(uint8_t val) {
    for (int i = 1 ; i <= 128 ; i <<= 1) {
        writePin(CLK, 0);
        writePin(DIN, (i & val) ? 1 : 0);
        writePin(CLK, 1);
    }
}


void sendData(uint8_t address, uint8_t val) {
    writePin(CS, 0);
    sendByte(address);
    sendByte(val);
    writePin(CS, 1);
}

void sendDataRev(uint8_t address, uint8_t val) {
    writePin(CS, 0);
    sendByte(address);
    sendByteRev(val);
    writePin(CS, 1);
}

uint8_t matrix[8] = {0};
#define MAXN 16
#define SAVED_BYTES (8 * MAXN)
uint8_t matrix_saved[SAVED_BYTES];
uint8_t matrix_n = 0;

void writeMatrix() {
    for (int i=0 ; i<8 ; ++i) {
        sendDataRev(i + 1, matrix[i]);
    }
}

void zeroMatrix() {
    for (int i=0 ; i<8 ; ++i) {
        matrix[i] = 0;
    }
}
void fillMatrix(uint8_t value) {
    for (int i=0 ; i<8 ; ++i) {
        matrix[i] = value;
    }
}


void setup() {
    // put your setup code here, to run once:

    PORTA.DIR = 2|4|8 | 16|32|64|128; //pa1, pa2, pa3 control the 8x8
    //pa4,pa5,pa6,pa7 send 

    PORTB.DIR = 0; //portb reads
    PORTB.PIN0CTRL |= 8;     //enabling pullups
    PORTB.PIN1CTRL |= 8;
    PORTB.PIN2CTRL |= 8;
    PORTB.PIN3CTRL |= 8;

    /* PORTA.PIN2CTRL |= 8;// + 3; //3 is falling edge interrupt; in power down only pin A2 can */

    sendData(DISPLAY_TEST, 0);
    sendData(INTENSITY, 1);
    sendData(SCAN_LIMIT, 0x0f); // "scan all digits"
    sendData(DECODE_MODE, 0); //bcd mode no ty
    sendData(SHUTDOWN, 1);

    for (int i=0 ; i<SAVED_BYTES ; ++i) {
        matrix_saved[i] = EEPROM.read(i);
    }
    moveMatrix(0);

    writeMatrix();
}

void Flip (void) {
    switch (click_state) {
    case CLICK_FULL:
        for (int i=0 ; i<8 ; ++i) {
            sendDataRev(i + 1, ~matrix[i]);
        }
        break;
    case CLICK_TOP_LEFT:
        for (int i=0 ; i<4 ; ++i) {
            sendDataRev(i + 1, 15 ^ matrix[i]);
        }
        break;
    case CLICK_TOP_RIGHT:
        for (int i=0 ; i<4 ; ++i) {
            sendDataRev(i + 1, (15 * 16) ^ matrix[i]);
        }
        break;
    case CLICK_BOTTOM_LEFT:
        for (int i=4 ; i<8 ; ++i) {
            sendDataRev(i + 1, 15 ^ matrix[i]);
        }
        break;
    case CLICK_BOTTOM_RIGHT:
        for (int i=4 ; i<8 ; ++i) {
            sendDataRev(i + 1, (15 * 16) ^ matrix[i]);
        }
        break;
    }
    delay(100);
    writeMatrix();
}

void saveMatrix(void) {
    int base = matrix_n * 8; 
    for (int i=0 ; i<8 ; ++i) {
        matrix_saved[base + i] = matrix[i];
        EEPROM.write(base + i, matrix[i]);
    }
}

void moveMatrix(int delta) {
    matrix_n = (matrix_n + MAXN + delta) % MAXN;
    int base = matrix_n * 8; 
    for (int i=0 ; i<8 ; ++i) {
        matrix[i] = matrix_saved[base + i];
    }
}

int xx = 0; 
void loop() {
    delay(25);
    int k = getKey();
    uint8_t mask_x;
//    k = xx;
    xx = (xx + 1) % 1000;
    if (!xx) {
        saveMatrix();
    }
    if (k >= 0 && k < 16) {
        int x = (k & 3);
        int y = ((k & 12) >> 2); 
        int y1 = y * 2, y2 = y * 2 + 1;

        switch(click_state) {
        case CLICK_FULL:
            mask_x = (1 << (2 * x)) + (1 << (2 * x + 1)); 
            if ((matrix[y1] & mask_x) == mask_x && (matrix[y2] & mask_x) == mask_x) {
                matrix[y1] &= ~mask_x;
                matrix[y2] &= ~mask_x;
            } else {
                matrix[y1] |= mask_x;
                matrix[y2] |= mask_x;
            }
            break;
        case CLICK_TOP_LEFT:
            mask_x = 1 << x; 
            if (matrix[y] & mask_x) {
                matrix[y] &= ~mask_x;
            } else {
                matrix[y] |= mask_x;
            }
            break;
        case CLICK_TOP_RIGHT:
            mask_x = 1 << (x + 4); 
            if (matrix[y] & mask_x) {
                matrix[y] &= ~mask_x;
            } else {
                matrix[y] |= mask_x;
            }
            break;
        case CLICK_BOTTOM_LEFT:
            mask_x = 1 << x; 
            if (matrix[y + 4] & mask_x) {
                matrix[y + 4] &= ~mask_x;
            } else {
                matrix[y + 4] |= mask_x;
            }
            break;
        case CLICK_BOTTOM_RIGHT:
            mask_x = 1 << (x + 4); 
            if (matrix[y + 4] & mask_x) {
                matrix[y + 4] &= ~mask_x;
            } else {
                matrix[y + 4] |= mask_x;
            }
            break;
        }
    }

    switch (k) {
    case COM_FULL:
        /* fillMatrix(129); */
        /* matrix[0] = matrix[7] = 255; */
        click_state = CLICK_FULL;
        Flip ();
        break;
    case COM_TOP_RIGHT:
        /* zeroMatrix(); */
        /* matrix[0] = matrix[3] = 15 * 16; */
        /* matrix[1] = matrix[2] = 9 * 16; */
        click_state = CLICK_TOP_RIGHT;
        Flip ();
        break;
    case COM_TOP_LEFT:
        /* zeroMatrix(); */
        /* matrix[0] = matrix[3] = 15; */
        /* matrix[1] = matrix[2] = 9; */
        click_state = CLICK_TOP_LEFT;
        Flip ();
        break;
    case COM_BOTTOM_RIGHT:
        /* zeroMatrix(); */
        /* matrix[4] = matrix[7] = 15 * 16; */
        /* matrix[5] = matrix[6] = 9 * 16; */
        click_state = CLICK_BOTTOM_RIGHT;
        Flip ();
        break;
    case COM_BOTTOM_LEFT:
        /* zeroMatrix(); */
        /* matrix[4] = matrix[7] = 15; */
        /* matrix[5] = matrix[6] = 9; */
        click_state = CLICK_BOTTOM_LEFT;
        Flip ();
        break;
    case COM_LEFT:
        saveMatrix();
        moveMatrix(-1); 
        break;
    case COM_RIGHT:
        saveMatrix();
        moveMatrix(1); 
        break;
    case COM_UP:
        break;
    case COM_DOWN:
        break;
    default:
        break;
    }
    writeMatrix();
}


#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>
#include <math.h>

#define STATE_OFF 100
#define STATE_SCAN 101

#define STATE_WIRE_NOT 102
#define STATE_AND_OR 103 
#define STATE_XOR_NAND 104
#define STATE_LATCH 105
#define STATE_SHIFT 106 
#define STATE_SEVEN 107

#define STATE_FAIL 108

#define SHUTDOWN_DELAY 80000
#define SCAN_DELAY 1250

#define MAX_HOLES 8
#define MAX_INTERVAL (1 + MAX_HOLES * 2)

uint8_t state = STATE_OFF;
uint8_t play_state = STATE_OFF;

long int last_time = 0;
int interval[MAX_INTERVAL];
int ninterval = 0; 
uint8_t latch_on; 

uint8_t shift_data[3];

#define LED0 0
#define LED1 1
#define LED2 2

#define HOLE_PIN 0
#define RED_BUT 1
#define BLUE_BUT 2

void writePin (uint8_t pin, uint8_t val) {
    switch(pin) {
    case LED0: //led from vcc to pb2; pin is set as inverted
        if (val) {
            PORTB.OUT |= 1 << 2; //set it 1 makes output low, led on
        } else {
            PORTB.OUT &= ~(1 << 2); //set i 0 makes output high, led off
        }
        break;
    case LED1: //led from pb1 to gnd
        if (val) {
            PORTB.OUT |= 1 << 1;
        } else {
            PORTB.OUT &= ~(1 << 1);
        }
        break;
    case LED2: //led from pb0 to gnd
        if (val) {
            PORTB.OUT |= 1;
        } else {
            PORTB.OUT &= ~1;
        }
        break;
    }
}


uint8_t readPin (uint8_t pin) {
    switch (pin) { //returns 1 when the button is pressed (which is a LOW reading)

    case HOLE_PIN: //pa2, which is the hole reader 
        return (PORTA.IN & (1 << 2)) == 0;
    case RED_BUT: //red button goes to pa6
        return (PORTA.IN & (1 << 6)) == 0;
    case BLUE_BUT: //blue button goes to pb3
        return (PORTB.IN & (1 << 3)) == 0;
    }
    return 0;
}

void setup (void) {
    // put your setup code here, to run once:
//set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    // high bits for outputs
    cli();
    PORTA.DIR = 0; //no outputs
    PORTB.DIR = 1 + 2 + 4; //PB0, PB1, PB2 outputs
    PORTB.PIN2CTRL |= 128; //INVERTED output pin

    //enabling pullups
//    PORTA.PIN2CTRL |= 8 + 3; //3 is falling edge interrupt; in power down only pin A2 can
    PORTA.PIN2CTRL |= 8 + 1; //1 is both edges interrupt; in power down only pin A2 can


    PORTA.PIN6CTRL |= 8; // input pullup
    PORTB.PIN3CTRL |= 8;
    writeAll(0);
    delay(10);
    sei();
}

void go_sleep (void) {
    state = STATE_OFF;
    while (state == STATE_OFF) {
        cli();
        set_sleep_mode(SLEEP_MODE_PWR_DOWN);
        sleep_enable();
        sei();
        sleep_cpu();
        sleep_disable();
    }    
}

void writeAll(int value) {
    writePin(LED0, value);
    writePin(LED1, value);
    writePin(LED2, value);
}

void writeMask(int value) {
    writePin(LED0, value & 4);
    writePin(LED1, value & 2);
    writePin(LED2, value & 1);
}

void DecideBarcode () {
    last_time = millis();


    int i, max_i = 0;
    if (0 == ninterval) {
        state = STATE_OFF;
        return;
    }
    
    ninterval = min(ninterval, MAX_INTERVAL);
    interval[0] = interval[ninterval - 1];
    for (i=1 ; i<ninterval ; ++i) {
        if (interval[i] > interval[max_i]) {
            max_i = i; 
        } 
    }
    switch (ninterval) {
    case 1: // no hole
        state = STATE_WIRE_NOT;
        break;
    case 3: //one hole
        state = STATE_AND_OR;
        break;
    case 5: //two holes
        if (max_i == 0 || max_i == 4) {
            state = STATE_XOR_NAND;            
        } else if (max_i == 2) {
            state = STATE_LATCH;             
            latch_on = 0; 
        } else /* if (max_i == 1 || max_i == 3) */ {
            state = STATE_FAIL;
        }
        break;
    case 7: //three holes
        if (max_i == 0 || max_i == 6) {
            state = STATE_SHIFT;
            shift_data[0] = shift_data[1] = shift_data[2] = 0;
        } else if (max_i == 2 || max_i == 4) {
            state = STATE_SEVEN;
        } else {
            state = STATE_FAIL;
        }
        break;
    default:
        state = STATE_FAIL;
    }
    if (state == STATE_FAIL) {
        state = STATE_OFF; 
    }
    /* switch(state) { */
    /* case STATE_WIRE_NOT: */
    /*     writeMask(1); */
    /*     break; */
    /* case STATE_AND_OR: */
    /*     writeMask(2); */
    /*     break; */
    /* case STATE_XOR_NAND: */
    /*     writeMask(3); */
    /*     break; */
    /* case STATE_LATCH: */
    /*     writeMask(4); */
    /*     break; */
    /* case STATE_SHIFT: */
    /*     writeMask(5); */
    /*     break; */
    /* case STATE_SEVEN: */
    /*     writeMask(6); */
    /*     break; */
    /* case STATE_FAIL: */
    /*     writeMask(7); */
    /*     break; */
    /* } */
    /* delay(500); */
}

int last_red = 0;
int last_blue = 0; 

void loop (void) {
    int red = readPin(RED_BUT);
    int blue = readPin(BLUE_BUT);

    if (state != STATE_OFF && state != STATE_SCAN) {
        if (red || blue) {
            last_time = millis();
        }

        if (millis() - last_time > SHUTDOWN_DELAY) {
            state = STATE_OFF;
        }
    }

    switch(state) {
    case STATE_OFF:
        writeAll(0);
        go_sleep();
        break;
    case STATE_SCAN:
        writeAll(0);
        if (millis() - last_time > SCAN_DELAY) {
            DecideBarcode();
            break;
        }
        break;

    case STATE_WIRE_NOT:
        writePin(LED0, red);
        writePin(LED1, blue);
        writePin(LED2, !blue);
        break;
    case STATE_AND_OR:
        writePin(LED0, red & blue);
        writePin(LED1, red | blue);
        writePin(LED2, 0);
        break;
    case STATE_XOR_NAND:
        writePin(LED0, red ^ blue);
        writePin(LED1, !(red & blue));
        writePin(LED2, 0);
        break;
    case STATE_LATCH:
        if (red) {
            latch_on = 0; 
        } else if (blue) {
            latch_on = 1; 
        }
        writePin(LED0, latch_on);
        writePin(LED1, !latch_on);
        writePin(LED2, 0);
        break;
    case STATE_SHIFT:
        if (blue && !last_blue) {
            shift_data[2] = shift_data[1];
            shift_data[1] = shift_data[0];
            shift_data[0] = red;
        }
        writePin(LED0, shift_data[0]);
        writePin(LED1, shift_data[1]);
        writePin(LED2, shift_data[2]);
        break;
    case STATE_SEVEN:
        writeMask(6);
        break;
    case STATE_FAIL:
        writeMask(7);
        break;

        /* writePin(LED0, readPin(HOLE_PIN)); */
        /* writePin(LED1, readPin(RED_BUT)); */
        /* writePin(LED2, readPin(BLUE_BUT)); */
    }

    last_red = red;
    last_blue = blue; 

    delay(10);
}


ISR(PORTA_PORT_vect) {
    // Clear the interrupt flag for the button
    
    switch (state) {
    case STATE_OFF:
    default: //all the game states come here
        state = STATE_SCAN;
        last_time = millis();
        ninterval = 0; 
        break;
    case STATE_SCAN: // acquire barcode
        long int time = millis();
        int dt = (time - last_time); 
        if (dt < 6) {
            break; //ignore bouncing
        }
        
        interval[ninterval++] = time - last_time;
        last_time = time;


        if (ninterval >= MAX_INTERVAL) {
            DecideBarcode();
        }
        break;
    }
    PORTA.INTFLAGS = 4;
}


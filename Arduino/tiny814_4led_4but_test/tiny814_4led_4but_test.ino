#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>

#define STATE_OFF 1
#define STATE_NEXT_LEVEL 2
#define STATE_PLAY 3
#define STATE_LOSE 4
#define STATE_WIN 5

#define MAX_LEVEL 36


uint8_t state = STATE_OFF;
uint8_t level = 0; 

uint8_t goal[MAX_LEVEL * 2 + 5];
uint8_t goal_n;
uint8_t progress = 0; 

long int last_time = 0; 

void initGoal() {
    if (level < MAX_LEVEL) {
        level += 1; 
    }
    progress = 1;  // starting with 1 makes it safe to check goal[progress-1]
    goal[0] = 0;
    goal_n = 1;
    delay(500);
    for (uint8_t i=0 ; i<level ; ++i) {
        uint8_t pin = random(4);
        writePin(pin, 1);        
        delay(700 - level * 10);
        writePin(pin, 0);
        if (i < level - 1) {
            delay(300 - level * 5);
        }
        goal[goal_n++] = 1 << pin;
        goal[goal_n++] = 0; 
    }
}


void writePin(uint8_t pin, uint8_t val) {
    switch(pin) {
    case 3:
        if (val) {
            PORTB.OUT |= 1 << 2;
        } else {
            PORTB.OUT &= ~(1 << 2);
        }
        break;
    case 2:
        if (val) {
            PORTB.OUT |= 1 << 3;
        } else {
            PORTB.OUT &= ~(1 << 3);
        }

        break;
    case 0:
        if (val) {
            PORTA.OUT |= 1 << 6;
        } else {
            PORTA.OUT &= ~(1 << 6);
        }

        break;
    case 1:
        if (val) {
            PORTA.OUT |= 1 << 7;
        } else {
            PORTA.OUT &= ~(1 << 7);
        }
        break;
    }
}

uint8_t readPin(uint8_t pin) {
    switch (pin) {
    case 3:
        return (PORTB.IN & (1 << 1)) == 0;
    case 2:
        return (PORTB.IN & (1 << 0)) == 0;
    case 1:
        return (PORTA.IN & (1 << 1)) == 0;
    case 0:
        return (PORTA.IN & (1 << 2)) == 0;
    }
    return 0;
}

void setup() {
    // put your setup code here, to run once:
//set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    // high bits for outputs
    cli();
    PORTA.DIR = 128 + 64; //PA6, PA7
    PORTB.DIR = 4 + 8; //PB2, PB3

    //enabling pullups
    PORTA.PIN1CTRL |= 8; //8 is pullup
    PORTA.PIN2CTRL |= 8 + 3; //3 is falling edge interrupt; in power down only pin A2 can
    PORTB.PIN0CTRL |= 8;
    PORTB.PIN1CTRL |= 8;
    delay(10);
    sei();
}

void go_sleep() {
    if (state == STATE_OFF) {
        cli();
        set_sleep_mode(SLEEP_MODE_PWR_DOWN);
        sleep_enable();
        sei();
        sleep_cpu();
        sleep_disable();
    }    
}

uint8_t getInputMask() {
    return readPin(0) + readPin(1) * 2 + readPin(2) * 4 + readPin(3) * 8;
}

void loop() {
    uint8_t buts;
    switch(state) {
    case STATE_OFF:
        go_sleep();
        state = STATE_WIN; 
        break;

    case STATE_NEXT_LEVEL:
        initGoal();
        state = STATE_PLAY;
        last_time = millis();
        break;

    case STATE_PLAY:
        if (millis () - last_time > 60000) {
            state = STATE_LOSE;
            return;
        }
        buts = getInputMask(); 
        if (goal[progress] == buts) {
            progress++;
            last_time = millis();
            if (progress >= goal_n) {
                state = STATE_WIN;
                return;
            }
        }
        if (buts != goal[progress] && buts != goal[progress - 1]) {
            state = STATE_LOSE;
            return;
        }

        for (uint8_t i=0 ; i<4 ; ++i) {
            writePin(i, readPin(i));
        }
        delay(10);
        break;
    case STATE_LOSE:
        writePin(0, 1);        
        writePin(1, 1);        
        writePin(2, 1);        
        writePin(3, 1);        
        delay(700);
        writePin(0, 0);        
        writePin(1, 0);        
        writePin(2, 0);        
        writePin(3, 0);        
        delay(10);
        state = STATE_OFF;
        break;
    case STATE_WIN:
        delay(200);
        for (int i=0 ; i<3 ; ++i) {
            writePin(1, 0);
            writePin(0, 1);
            delay(70);
            writePin(0, 0);
            writePin(1, 1);
            delay(70);
            writePin(1, 0);
            writePin(2, 1);
            delay(70);
            writePin(2, 0);
            writePin(3, 1);
            delay(70);
            writePin(3, 0);
            writePin(2, 1);
            delay(70);
            writePin(2, 0);
            writePin(1, 1);
            delay(70);
        }
        writePin(1, 0);
        writePin(0, 1);
        delay(70);
        writePin(0, 0);
        state = STATE_NEXT_LEVEL;
        break;
    }
}

ISR(PORTA_PORT_vect) {
    // Clear the interrupt flag for the button
    PORTA.INTFLAGS = 4;
    last_time = millis();
    if (state == STATE_OFF) {
        state = STATE_NEXT_LEVEL;
        level = 0;
    }
}

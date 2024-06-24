#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>


#define RED 6
#define YELLOW 7
#define GREEN 1

#define BIG_DELAY 12000
#define SMALL_DELAY 4000


int count = 0; 

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


void go_sleep (void) {
    cli();
    set_sleep_mode(SLEEP_MODE_PWR_DOWN);
    sleep_enable();
    sei();
    sleep_cpu();
    sleep_disable();
}


void setup() {
    // put your setup code here, to run once:
    //PORTA.DIR &= ~(1 << INPIN);
    PORTA.DIR = (1 << RED) + (1 << GREEN) + (1 << YELLOW);
    PORTA.PIN2CTRL |= 8 + 3;  //8 for pullup; 3 for falling edge interrupt enable

    //PORTA.PIN1CTRL |= 8;
    writePin(GREEN, 0);
    writePin(RED, 0);
    writePin(YELLOW, 0);
}

void Light(int pin) {
    writePin(YELLOW, 0);
    writePin(pin, 1);
    delay(BIG_DELAY);

    writePin(pin, 0);
    writePin(YELLOW, 1);
    delay(SMALL_DELAY);
}

void loop() {
    if (++count > 15) {
        writePin(YELLOW, 0);
        go_sleep();
        count = 0; 
    }
    
    Light(RED);
    Light(GREEN);
}


ISR(PORTA_PORT_vect) {
    // Clear the interrupt flag for the button
    count = 0; 
    PORTA.INTFLAGS |= 4;
}

#include <avr/io.h>
#include <avr/sleep.h>
#include <avr/interrupt.h>

#define STATE_OFF 1
#define STATE_MEMORY_NEXT_LEVEL 2
#define STATE_MEMORY_PLAY 3
#define STATE_LOSE 4
#define STATE_LOSE_NEW_RECORD 5
#define STATE_MEMORY_WIN 6

#define STATE_WHACK 7
#define STATE_ORDERED_WHACK 8

#define STATE_RHYTHM 9
#define STATE_RHYTHM_WIN 10

#define MAX_MEMORY_LEVEL 72
#define MAX_RHYTHM 16
#define RHYTHM_LIT_START 8
#define RHYTHM_LIT_STOP 20


uint8_t whack = 0; //mask of which lights are lit
uint8_t o_whack[4] = {0}; //spawn order of lights

int whack_count = 0; //timer until spawn

uint8_t state = STATE_OFF;
int level = 0; //used by all 4 game modes
int whack_record_level = 0;
int whack_ordered_record_level = 0;
int memory_record_level = 0; 

uint8_t goal[MAX_MEMORY_LEVEL + 3]; 
uint8_t goal_n; 
uint8_t progress = 0; 

signed char pins_last = 0; 
long int last_time = 0; 


int rhythm_record_level = 0;
int rhythm[3][MAX_RHYTHM];
int nrhythm[3];

int rhythm_progress[3];
int rhythm_last[3];
int rhythm_quit_counter = 0;

int rhythm_period = 0;
int rhythm_now = 0; 
int rhythm_no_key_count = 0;
int rhythm_required_bars = 0;


int whackCD (void) {
    if (level > 230) {
        return 20;
    }
    if (level > 130) {
        return 30 - (level - 130) / 10; 
    }
    if (level > 80) {
        return 40 - (level - 80) / 5;
    }
    if (level > 60) {
        return 60 - (level - 60);
    }
    if (level > 40) {
        return 100 - (level - 40) * 2;
    }
    return 500 - level * 10;
}

void whackLose(void) {
    switch(state) {
    case STATE_ORDERED_WHACK:
        if (level > whack_ordered_record_level) {
            whack_ordered_record_level = level;

            state = STATE_LOSE_NEW_RECORD;
        } else {
            state = STATE_LOSE;
        }
        break;
    case STATE_WHACK:
        if (level > whack_record_level) {
            whack_record_level = level;
            state = STATE_LOSE_NEW_RECORD;
        } else {
            state = STATE_LOSE;            
        }
        break;
    }
}


#define addBeat(pin, time) do {rhythm[pin][nrhythm[pin]++] = time * beat + 2;} while (0)

void rhythmSpawn (void) {
    int beat = 32;

    state = STATE_RHYTHM;

    nrhythm[2] = nrhythm[1] = nrhythm[0] = 0;
    rhythm_last[2] = rhythm_last[1] = rhythm_last[0] = -1;
    rhythm_progress[2] = rhythm_progress[1] = rhythm_progress[0] = 0;

    rhythm_now = 0;
    rhythm_no_key_count = 0;
    rhythm_required_bars = 2;
    
    switch(level++) {
    case 0:
        beat = 32;
        rhythm_period = beat * 8;
        addBeat(0, 0);
        addBeat(0, 2);
        addBeat(0, 4);
        addBeat(0, 5);
        addBeat(0, 6);
        break;
    case 1:
        beat = 32;
        rhythm_period = beat * 12;
        addBeat(0, 0);
        addBeat(0, 4);
        addBeat(1, 8);
        addBeat(1, 9);
        addBeat(1, 10);
        addBeat(1, 11);
        break;
    case 2:
        beat = 24;
        rhythm_period = beat * 12;
        addBeat(0, 0);
        addBeat(0, 3);
        addBeat(1, 6);
        addBeat(1, 8);
        addBeat(1, 10);
        break;
    case 3:
        beat = 24;
        rhythm_period = beat * 12;
        addBeat(0, 0);
        addBeat(0, 3);
        addBeat(0, 6);
        addBeat(0, 9);
        addBeat(1, 1);
        addBeat(1, 2);
        addBeat(2, 4);
        addBeat(2, 5);
        addBeat(1, 7);
        addBeat(1, 8);
        addBeat(2, 10);
        addBeat(2, 11);
        break;
    case 4:
        beat = 24;
        rhythm_period = beat * 6;
        addBeat(0, 0);
        addBeat(0, 3);
        addBeat(1, 0);
        addBeat(1, 2);
        addBeat(1, 4);
        break;
    case 5:
        beat = 32;
        rhythm_period = beat * 14;
        addBeat(0, 0);
        addBeat(1, 2);
        addBeat(2, 4);
        addBeat(0, 6);
        addBeat(1, 8);
        addBeat(2, 10);
        addBeat(0, 11);
        addBeat(1, 12);
        addBeat(2, 13);
        break;
    default:
        level = 0;
        state = STATE_LOSE;
    }
}

#undef addBeat

void whackSpawn (void) {
    level++;
    uint8_t ok[4];
    uint8_t n = 0;
    for (uint8_t i=0 ; i<4 ; ++i) {
        if (!(whack & (1 << i))) {
            ok[n++] = i;
        }
    }
    if (n <= 1) {
        whackLose();
    }

    uint8_t spawn = ok[random(n)];
    o_whack[4 - n] = spawn;
    whack |= (1 << spawn);
    whack_count = whackCD();
    switch(n) {
    case 4:
        level += 2;
        break;
    case 3:
        whack_count += whack_count / 3;
        break;
    case 2:
        whack_count += (whack_count * 2) / 3;
        break;
    }
}

void writePin (uint8_t pin, uint8_t val) {
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


void initMemoryGoal () {
    int lev;

    level++;

    if (level < MAX_MEMORY_LEVEL-1) {
        lev = level;
    } else {
        lev = MAX_MEMORY_LEVEL-1;
    }
    progress = 0;
    goal_n = 0;
    delay(500);
    for (int i=0 ; i<lev ; ++i) {
        uint8_t pin = random(4);
        writePin(pin, 1);
        delay(700 - lev * 5);
        writePin(pin, 0);
        if (i < lev - 1) {
            delay(300 - lev * 2);
        }
        goal[goal_n++] = pin;
    }
    state = STATE_MEMORY_PLAY;
    last_time = millis();
}



uint8_t readPin (uint8_t pin) {
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

signed char getPress (void) {
    signed char ret = -1; 
    for (signed char i=0 ; i<4 ; ++i) {
        if (readPin(i)) {
            if (!(pins_last & (1 << i))) {
                ret = i;
            }
        } else {
            pins_last &= ~(1 << i);
        }
    }
    if (ret >= 0) {
        pins_last |= (1 << ret);
    }
    return ret; 
}


void setup (void) {
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

void go_sleep (void) {
    while (state == STATE_OFF) {
        cli();
        set_sleep_mode(SLEEP_MODE_PWR_DOWN);
        sleep_enable();
        sei();
        sleep_cpu();
        sleep_disable();
    }    
}

uint8_t getInputMask (void) {
    return readPin(0) + readPin(1) * 2 + readPin(2) * 4 + readPin(3) * 8;
}

void memoryLose(void) {
    if (level > memory_record_level) {
        memory_record_level = level;
        state = STATE_LOSE_NEW_RECORD;
    } else {
        state = STATE_LOSE;
    }
}

int rhythmHit(int pin) {
    for (int i=0 ; i<nrhythm[pin] ; ++i) {
        if ((rhythm_now >= rhythm[pin][i]) && (rhythm_now <= rhythm[pin][i] + RHYTHM_LIT_STOP)) {
            return i;
        }
    }
    return -1;
}

int rhythmHitAny(void) {
    for (int i=0 ; i<3 ; ++i) {
        int ret = rhythmHit(i);
        if (ret >= 0) {
            return 1;
        }
    }
    return 0;
}


void rhythmResetProgress(void) {
    rhythm_last[2] = rhythm_last[1] = rhythm_last[0] = -1;
    rhythm_progress[2] = rhythm_progress[1] = rhythm_progress[0] = 0;
}

void loopRhythm(void) {
    int but;
    rhythm_now = (rhythm_now + 1) % rhythm_period;
    writeAll(0);
    while ((but = getPress()) >= 0) {
        if (but == 3) {
            rhythm_quit_counter = 0; 
            continue;
        } 
        rhythm_no_key_count = 0;
            
        int hit = rhythmHit(but);
        if (-1 == hit) {
            rhythmResetProgress();
            continue;
        }
        if (rhythm_last[but] == -1) {
            rhythm_last[but] = hit;
            rhythm_progress[but] = 1;
            continue;
        }
        rhythm_last[but] = hit;
        rhythm_progress[but] += 1;
    }
    if (readPin(3)) {
        writePin(3, 1);
        if (rhythm_quit_counter++ > 100) {
            state = STATE_LOSE;
            return;
        }
    } else {
        if (rhythm_quit_counter) {
            rhythm_quit_counter = 0; 
            rhythmSpawn();
            return;
        }
    }
    if (rhythm_no_key_count++ > 3000) {
        state = STATE_LOSE;
        return;
    }


    int last_time = -1;
    int prev_time = -1;
    for (int i=0 ; i<3 ; ++i) {
        for (int j=0 ; j<nrhythm[i] ; ++j) {
            int t = rhythm[i][j] + RHYTHM_LIT_STOP;
            if (rhythm_now > t && prev_time < t) {
                prev_time = t;
            }
            if (last_time < t) {
                last_time = t;
            }
        }
    }
    if (prev_time < 0) {
        prev_time = last_time; 
    }
    for (int i=0 ; i<3 ; ++i) {
        if (!nrhythm[i]) {
            continue;
        }
        int prev = nrhythm[i] - 1; 
        for (int j=0 ; j<nrhythm[i] ; ++j) {
            if (rhythm_now >= rhythm[i][j] + RHYTHM_LIT_START && 
                rhythm_now <= rhythm[i][j] + RHYTHM_LIT_STOP) 
            {
                writePin(i, 1);
            }
            if (rhythm_now > rhythm[i][j] + RHYTHM_LIT_STOP) {
                prev = j;
            }
        }
        int t = rhythm[i][prev] + RHYTHM_LIT_STOP;
        if (!rhythmHitAny() && prev != rhythm_last[i] && t == prev_time) {
            rhythmResetProgress();
        }
    }
    writePin(3, rhythm_progress[0] || rhythm_progress[1] || rhythm_progress[2]);
    for (int i=0 ; i<3 ; ++i) {
        if (rhythm_required_bars * nrhythm[i] > rhythm_progress[i]) {
            return;
        }
    }
    state = STATE_RHYTHM_WIN;
}

void loopWhack(void) {
    int but;
    if (!whack) {
        whack_count = min(whack_count, 50);
    }

    if (--whack_count < 0) {
        whackSpawn();
        if (state != STATE_WHACK && state != STATE_ORDERED_WHACK) {
            return; 
        }
    }
    but = getPress();
    if (but >= 0) {
        bool order_ok = (state != STATE_ORDERED_WHACK) || 
            (o_whack[0] == but);
        if ((whack & (1 << but)) && order_ok) {
            whack &= ~(1 << but);
            for (uint8_t i=0 ; i<3 ; ++i) {
                o_whack[i] = o_whack[i + 1];
            }
        } else {
            whackLose();
            return;
        }
    }
    for (uint8_t i=0 ; i<4 ; ++i) {
        writePin(i, whack & (1 << i));
    }
}

void loopMemory(void) {
    int but; 
    for (int i=0 ; i<4 ; ++i) {
        writePin(i, readPin(i));
    }
    if (millis () - last_time > 60000) {
        memoryLose();
        return;
    }
    but = getPress(); 
    if (but < 0) {
        return;
    }
    if (goal[progress] == but) {
        progress++;
        last_time = millis();
        if (progress >= goal_n) {
            state = STATE_MEMORY_WIN;
            return;
        }
    } else {
        memoryLose();
        return;
    }
}

void writeAll(int value) {
    writePin(0, value);
    writePin(1, value);
    writePin(2, value);
    writePin(3, value);
}

void loopLose(void) {
    writeAll(1);
    delay(700);
    writeAll(0);
    state = STATE_OFF;    
}

void loopLoseNewRecord(void) {
    for (uint8_t i=0 ; i<5 ; ++i) {
        writeAll(1);
        delay(300);
        writeAll(0);
        if (i < 4) {
            delay(200);
        }
    }
    state = STATE_OFF;
}

void movePin(int src_pin, int dest_pin, int time) {
    writePin(src_pin, 0);
    writePin(dest_pin, 1);
    delay(time);
}

void loopWin(void) {
    delay(200);
    for (int i=0 ; i<3 ; ++i) {
        movePin(1, 0, 50);
        movePin(0, 1, 50);
        movePin(1, 2, 50);
        movePin(2, 3, 50);
        movePin(3, 2, 50);
        movePin(2, 1, 50);
    }
    movePin(1, 0, 50);
    writePin(0, 0);
    switch(state) {
    case STATE_MEMORY_WIN:
        state = STATE_MEMORY_NEXT_LEVEL;
        break;
    case STATE_RHYTHM_WIN:
        rhythmSpawn();
        break;
    }
}

void loop (void) {
    delay(10);
    switch(state) {
    case STATE_OFF:
        go_sleep();
        break;
    case STATE_RHYTHM:
        loopRhythm();
        break;
    case STATE_ORDERED_WHACK:
    case STATE_WHACK:
        loopWhack();
        break;
    case STATE_MEMORY_NEXT_LEVEL:
        initMemoryGoal();
        break;
    case STATE_MEMORY_PLAY:
        loopMemory();
        break;
    case STATE_LOSE:
        loopLose();
        break;
    case STATE_LOSE_NEW_RECORD:
        loopLoseNewRecord();
        break;
    case STATE_MEMORY_WIN:
    case STATE_RHYTHM_WIN:
        loopWin();
        break;
    }
}

ISR(PORTA_PORT_vect) {
    // Clear the interrupt flag for the button
    PORTA.INTFLAGS = 4;
    last_time = millis();
    if (state == STATE_OFF) {
        randomSeed(last_time);
        pins_last = getInputMask();

        if (readPin(3)) {
            state = STATE_MEMORY_NEXT_LEVEL;
            level = 0;
        } else if (readPin(1)) {
            state = STATE_ORDERED_WHACK; 
            level = 0; 
            whack = 0;
            whackSpawn();
        } else if (readPin(2)) {
            state = STATE_RHYTHM;
            level = 0;
            rhythmSpawn();
        } else {
            state = STATE_WHACK; 
            level = 0; 
            whack = 0;
            whackSpawn();
        }
    }
}

/*
  Melody

  Plays a melody

  circuit:
  - 8 ohm speaker on digital pin 8

  created 21 Jan 2010
  modified 30 Aug 2011
  by Tom Igoe

  This example code is in the public domain.

  https://www.arduino.cc/en/Tutorial/BuiltInExamples/toneMelody
*/

#include "pitches.h"

/* // notes in the melody: */
/* const uint16_t melody[]  = { */
/*     NOTE_C4, NOTE_G3, NOTE_G3, NOTE_A3, NOTE_G3, 0, NOTE_B3, NOTE_C4 */
/* }; */

const uint16_t melody[]  = {
    NOTE_C5, NOTE_G4, NOTE_G4, NOTE_A4, NOTE_G4, 0, NOTE_B4, NOTE_C5
};


// note durations: 4 = quarter note, 8 = eighth note, etc.:
const char  noteDurations[]  = {
  4, 8, 8, 4, 4, 4, 4, 4
};

void setup() {
    /* for (int x=NOTE_A3 ; x<=NOTE_C4 ; x+=2)  { */
    /*     tone(A1, x, 100); */
    /*     delay(200); */
    /* } */

    delay(1000);

    // iterate over the notes of the melody:
    for (int i=0 ; i<3 ; ++i) {
        for (int thisNote = 0; thisNote < 8; thisNote++) {
            int noteDuration = 1000 / (int)noteDurations[thisNote];
            tone(A1, (int)melody[thisNote], noteDuration);

            // to distinguish the notes, set a minimum time between them.
            // the note's duration + 30% seems to work well:
            int pauseBetweenNotes = noteDuration * 1.30;
            delay(pauseBetweenNotes);
            // stop the tone playing:
            noTone(A1);
        }
        delay(250);
    }

    tone(A1, NOTE_C3);
    delay(2000);
    noTone(A1);
}

void loop() {
  // no need to repeat the melody.
}



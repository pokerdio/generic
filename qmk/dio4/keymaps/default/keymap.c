#include QMK_KEYBOARD_H

enum custom_keycodes {
    K1 = SAFE_RANGE,
    K2,
    K3,
    K4,
    K5
};

/*
 * State of our input language.
 *
 * IDLE:
 *     no extended gesture yet
 *
 * FIRST:
 *     one key has been pressed; if everything is released now,
 *     it becomes Esc/Tab/Space/Backspace/Enter.
 *
 * CONS:
 *     ambiguous consonant root such as 31 -> t / 313 -> . / 311 -> d
 *
 * CONT:
 *     a character has been produced and its continuation table is active.
 */
enum gesture_state {
    IDLE,
    FIRST,
    CONS,
    CONT,
    FAIL,
    MODIFIER, MODE_SINGLE, MODE_TYPING, PUNCT, REPEAT,
};

static enum gesture_state state = IDLE;

/* Bit mask of keys physically held right now. */
static uint8_t held = 0;

/* First and second presses of the current gesture. */
static uint8_t first  = 0;
static uint8_t second = 0;

/* Pending consonant for an ambiguous two-key consonant root. */
static uint16_t pending = KC_NO;

/* ---------- output helpers ---------- */

/* Output assumes the host uses a US layout for punctuation and symbols. */
static uint8_t active_mods;
static bool permanent_mods;
static uint8_t single_mode, typing_mode, selected_mode;
static bool selector_ready, modifier_explicit;
static uint16_t hold_started, repeat_at;

#ifndef GESTURE_REPEAT_DELAY
#    define GESTURE_REPEAT_DELAY 1000
#endif
#ifndef GESTURE_REPEAT_INTERVAL
#    define GESTURE_REPEAT_INTERVAL 70
#endif

static void clear_modifiers(void) {
    del_mods(active_mods);
    active_mods = 0;
    permanent_mods = false;
    send_keyboard_report();
}

static void output(uint16_t kc) {
    if (kc == KC_NO) {
	return;
    }
    /* tap_code16's synthetic Shift can otherwise remove a held Shift.
     * Restore our modifier mask after the tap, then consume one-shot mods. */
    tap_code16(kc);
    add_mods(active_mods);
    if (!permanent_mods) {
	clear_modifiers();
    } else {
	send_keyboard_report();
    }
}

static uint16_t single_key_output(uint8_t key) {
    static const uint16_t modes[6][4] = {
        {KC_TAB, KC_SPC, KC_BSPC, KC_ENT},
        {KC_LEFT, KC_UP, KC_DOWN, KC_RGHT},
        {S(KC_9), S(KC_0), KC_LBRC, KC_RBRC},
        {S(KC_LBRC), S(KC_RBRC), S(KC_COMM), S(KC_DOT)},
        {KC_HOME, KC_PGUP, KC_PGDN, KC_END},
        {KC_SLSH, KC_BSLS, S(KC_BSLS), S(KC_MINS)}
    };
    return key >= 2 && key <= 5 ? modes[single_mode][key-2] : KC_NO;
}

static void escape_action(void) {
    if (active_mods) {
	clear_modifiers();
    } else if (single_mode) {
	single_mode = 0;
    } else if (typing_mode) {
	typing_mode = 0;
    } else {
	output(KC_ESC);
    }
}

static uint16_t numeric_output(uint8_t a, uint8_t b) {
    uint8_t digit = 0;
    switch (a*10+b) {
    case 21: digit=1; break; case 23: digit=2; break;
    case 24: digit=3; break; case 25: digit=4; break;
    case 31: digit=5; break; case 32: digit=6; break;
    case 34: digit=7; break; case 35: digit=8; break;
    case 41: digit=9; break; case 42: digit=10; break;
    }
    if (digit) return typing_mode == 2 ? KC_F1+digit-1 :
                       digit == 10 ? KC_0 : KC_1+digit-1;
    if (typing_mode == 2) {
        if (a*10+b == 43) return KC_F11;
        if (a*10+b == 45) return KC_F12;
        return KC_NO;
    }
    switch (a*10+b) {
    case 43: return KC_MINS;
    case 45: return KC_DOT; 
    case 51: return S(KC_8);
    case 52: return KC_SLSH; 
    case 53: return S(KC_6);
    case 54: return KC_EQL;
    }
    return KC_NO;
}

/* ---------- vowel continuation ---------- */

/*
 * key = physical key 1..5.
 *
 * These implement:
 *
 * a(nrstl)
 * e(nrstl)
 * i(nrstc)
 * o(nrsfu)
 * u(nrstl)
 */

static bool is_vowel(uint16_t kc)
{
    return kc == KC_A ||
           kc == KC_E ||
           kc == KC_I ||
           kc == KC_O ||
           kc == KC_U;
}

static uint16_t continuation(uint16_t previous, uint8_t key)
{
    /*
     * Every consonant has the default vowel continuation:
     *
     * 1 2 3 4 5
     * a e i o u
     *
     * except the exceptions - the 5/u continuation is replaced by letter specific
     */

    if (!is_vowel(previous)) {
        switch (key) {
        case 1: return KC_A;
        case 2: return KC_E;
        case 3: return KC_I;
        case 4: return KC_O;
        case 5: 
	    switch (previous) {
	    case KC_S:
		return KC_S;
	    case KC_W:
	    case KC_C:
	    case KC_T:
	    case KC_G:
		return KC_H;
	    case KC_X:
	    case KC_M:
		return KC_P;
	    case KC_P:
	    case KC_D:
	    case KC_F:
		return KC_R;
	    case KC_R:
		return KC_S;
	    case KC_N:
		return KC_D;
	    case KC_L:
		return KC_L;
	    case KC_K:
		return KC_N;
	    default: return KC_U;
	    }
        }
    }

    /*
     * Vowels have their individual continuation alphabets.
     */

    switch (previous) {

    /* a(nrstl) */
    case KC_A:
        switch (key) {
        case 1: return KC_N;
        case 2: return KC_R;
        case 3: return KC_S;
        case 4: return KC_T;
        case 5: return KC_L;
        }
        break;

    /* e(nrstl), preserved from supplied table */
    case KC_E:
        switch (key) {
        case 1: return KC_N;
        case 2: return KC_R;
        case 3: return KC_S;
        case 4: return KC_T;
        case 5: return KC_L;
        }
        break;

    /* i(nrstc) */
    case KC_I:
        switch (key) {
        case 1: return KC_N;
        case 2: return KC_R;
        case 3: return KC_S;
        case 4: return KC_T;
        case 5: return KC_C;
        }
        break;

    /* o(nrsfu) */
    case KC_O:
        switch (key) {
        case 1: return KC_N;
        case 2: return KC_R;
        case 3: return KC_S;
        case 4: return KC_F;
        case 5: return KC_U;
        }
        break;

    /* u(nrstl) */
    case KC_U:
        switch (key) {
        case 1: return KC_N;
        case 2: return KC_R;
        case 3: return KC_S;
        case 4: return KC_T;
        case 5: return KC_L;
        }
        break;
    }

    return KC_NO;
}

static uint16_t vowel_root(uint8_t a, uint8_t b) {
    switch ((int)a*10+b) {
    case 21: return KC_A;
    case 23: return KC_I;
    case 24: return KC_O;
    case 25: return KC_U;
    case 32: return KC_E;
    default: return KC_NO;
    }
}

static uint16_t consonant_root(uint8_t a, uint8_t b)
{
    switch ((int)a*10+b) {
    case 31: return KC_L;
    case 34: return KC_W;
    case 35: return KC_H;

    case 41: return KC_S;
    case 42: return KC_C;
    case 43: return KC_B;

    case 51: return KC_T;
    case 52: return KC_M;
    case 53: return KC_D;

    default: return KC_NO;
    }
}

static bool consonant_unambiguous (uint16_t kc) {
    switch (kc) {
    case KC_T:
    case KC_S:
	return 1;
    default:
	return 0;
    }
}


/*
 * Does a third press supersede the pending consonant?
 *
 * Return KC_NO if it doesn't.
 */
static uint16_t consonant_override(uint8_t a, uint8_t b, uint8_t c)
{
    int ab = (int)a * 10 + b;
    /*
     * 31 is special:
     *
     * 313 -> "li"
     * 311 -> y
     *
     * Handle 313 separately in press_key().
     */
    if (ab == 31) {
        if (c == 1) return KC_Y;
    }


    if (ab == 34) {
	// 343 is special and handled in press_key
        if (c == 4) return KC_V;
    }

    if (ab == 35) {
        if (c == 3) return KC_X;
        if (c == 5) return KC_J;
    }

    if (ab == 41) {
        if (c == 4) return KC_Z;
        if (c == 1) return KC_X;
    }

    if (ab == 42) {
        if (c == 4) return KC_Q;
        if (c == 2) return KC_K;
    }

    if (ab == 43) {
        if (c == 4) return KC_F;
        if (c == 3) return KC_P;
    }

    if (ab == 52) {
        if (c == 5) return KC_R;
        if (c == 2) return KC_N;
    }

    if (ab == 53) {
        if (c == 5) return KC_Z;
        if (c == 3) return KC_G;
    }

    return KC_NO;
}

/* ---------- state machine ---------- */

static void reset_gesture(void)
{
    state   = IDLE;
    first   = 0;
    second  = 0;
    pending = KC_NO;
    selector_ready = false;
    modifier_explicit = false;
}


static void press_key(uint8_t key)
{
    uint16_t kc;

    switch (state) {
    case FAIL:
    case REPEAT:
        return;
    case MODIFIER:
        modifier_explicit = true;
        if (key == 1) {
            /* Empty permanence has no reset-visible state; keep this flag
             * within the gesture so a later modifier can still be permanent. */
            permanent_mods = !permanent_mods;
        } else {
            static const uint8_t masks[4] = {
                MOD_BIT(KC_LSFT), MOD_BIT(KC_LALT),
                MOD_BIT(KC_LCTL), MOD_BIT(KC_LGUI)
            };
            uint8_t mask = masks[key-2];
            active_mods ^= mask;
            if (active_mods & mask) add_mods(mask);
            else del_mods(mask);
            send_keyboard_report();
        }
        return;
    case MODE_SINGLE:
        /* Recognized selectors ignore trailing presses and commit at all-up. */
        selected_mode = key == 5 ? 0 : key+1;
        selector_ready = true;
        state = FAIL;
        return;
    case MODE_TYPING:
        if (key == 2 || key == 3) {
            selected_mode = key; /* 2 means number+Shift; 3 means F keys */
            selector_ready = true;
        } else selector_ready = false; /* Invalid 141/144/145 cancels selection. */
        state = FAIL;
        return;
    case PUNCT: {
        static const uint16_t dots[5] = {
            S(KC_SLSH), S(KC_1), KC_MINS, S(KC_GRV), KC_DOT
        };
        static const uint16_t commas[5] = {
            KC_SCLN, S(KC_SCLN), S(KC_MINS), S(KC_QUOT), KC_QUOT
	};
	output(first == 4 ? dots[key-1] : commas[key-1]);
	if (!(first == 4 && key == 5)) {
	    state = FAIL;
	}
        return;
    }
    case IDLE:
        first = key;
        hold_started = timer_read();
        state = FIRST;
        return;

    case FIRST:
        second = key;
        if (first == 1) {
            if (key == 2) {
                clear_modifiers();
                state = MODIFIER;
            } else if (key == 3 || key == 4) {
                selected_mode = 1;
                selector_ready = true;
                state = key == 3 ? MODE_SINGLE : MODE_TYPING;
            } else state = FAIL;
            return;
        }
        if (typing_mode) {
            output(numeric_output(first, key));
            state = FAIL;
            return;
        }
        if ((first == 4 && key == 5) || (first == 5 && key == 4)) {
            state = PUNCT;
            return;
        }

        /* Vowels are unambiguous and fire immediately. */
        kc = vowel_root(first, second);

        if (kc != KC_NO) {
            output(kc);
            pending = kc;
            state = CONT;
            return;
        }

        /* Consonants remain pending. */
        kc = consonant_root(first, second);


	/* except... */
	if (consonant_unambiguous(kc)) {
	    output(kc);
	    pending = kc;
	    state = CONT;
	    return;
	}

	/* but the others remain pending  */
        if (kc != KC_NO) {
            pending = kc;
            state = CONS;
            return;
        }

        /*
         * Invalid extended gesture for now.
         * Silently wait for all-up reset.
         */
	state = FAIL;
        return;


    case CONS:
        /*
         * Special 313 -> "li".
         */
        if (first == 3 && second == 1 && key == 3) {
            output(KC_L);
            output(KC_I);
            pending = KC_I;
            state = CONT;
            return;
        }

        /*
         * Special 343 -> "wi".
         */
        if (first == 3 && second == 4 && key == 3) {
            output(KC_W);
            output(KC_I);
            pending = KC_I;
            state = CONT;
            return;
        }

        kc = consonant_override(first, second, key);

        if (kc != KC_NO) {
            output(kc);

            /*
             * Punctuation terminates the gesture.
             * Further presses before all-up are ignored.
             */
            if (kc == KC_DOT  ||
                kc == KC_COMM ||
                kc == KC_SCLN ||
                kc == KC_EXLM ||
                kc == KC_QUES) {

                pending = KC_NO;
                state = FAIL;
                return;
            }

            pending = kc;
            state = CONT;
            return;
        }

        /*
         * Third key wasn't an override.
         *
         * Therefore the pending root consonant is confirmed.
         */
        output(pending);
        kc = continuation(pending, key);
        if (kc != KC_NO) {
            output(kc);
	    pending = kc;
	    state = CONT;
	} else {
	    state = FAIL;
	}

        return;
    case CONT:
        kc = continuation(pending, key);

        if (kc != KC_NO) {
            output(kc);
            pending = kc;
        }

        return;
    }
}


/* ---------- QMK interface ---------- */

static uint8_t key_number(uint16_t keycode)
{
    switch (keycode) {
    case K1: return 1;
    case K2: return 2;
    case K3: return 3;
    case K4: return 4;
    case K5: return 5;
    }

    return 0;
}


/* Firmware-generated taps give stable repeat speed across hosts.
 * Once repetition starts all combinations are rejected until all-up. */
void matrix_scan_user(void) {
    if (state == FIRST && first >= 2 &&
        timer_elapsed(hold_started) >= GESTURE_REPEAT_DELAY) {
        output(single_key_output(first));
        repeat_at = timer_read();
        state = REPEAT;
    } else if (state == REPEAT &&
               timer_elapsed(repeat_at) >= GESTURE_REPEAT_INTERVAL) {
        output(single_key_output(first));
        repeat_at = timer_read();
    }
}

bool process_record_user(uint16_t keycode, keyrecord_t *record)
{
    uint8_t key = key_number(keycode);

    if (!key)
        return true;

    uint8_t bit = 1 << (key - 1);

    if (record->event.pressed) {

        held |= bit;
        press_key(key);

    } else {

        held &= ~bit;
        if (state == REPEAT && key == first) state = FAIL;

        /*
         * ALL-UP is our gesture delimiter.
         */
        if (held == 0) {

            if (state == FIRST) {
                /*
                 * Nothing followed the first press:
                 * ordinary Esc/Tab/Space/Backspace/Enter.
                 */
                if (first == 1) escape_action();
                else output(single_key_output(first));

            } else if (state == CONS) {
                /*
                 * Ambiguous consonant was terminated by
                 * releasing everything.
                 */
                output(pending);
            }

            if (state == PUNCT) output(first == 4 ? KC_DOT : KC_COMM);
            if (state == MODIFIER) {
                if (!modifier_explicit) {
                    active_mods = MOD_BIT(KC_LSFT);
                    add_mods(active_mods);
                    send_keyboard_report();
                }
                if (!active_mods) permanent_mods = false;
            }
            if (selector_ready) {
                if (first == 1 && second == 3) single_mode = selected_mode;
                else if (first == 1 && second == 4) {
                    typing_mode = selected_mode == 3 ? 2 : 1;
                    if (selected_mode == 2) {
                        clear_modifiers();
                        active_mods = MOD_BIT(KC_LSFT);
                        add_mods(active_mods);
                        send_keyboard_report();
                    }
                }
            }
            reset_gesture();
        }
    }

    return false;
}


const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        K1, K2, K3, K4, K5
    )
};



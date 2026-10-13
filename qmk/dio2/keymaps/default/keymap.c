/* #include QMK_KEYBOARD_H */

/* const uint16_t PROGMEM keymaps [][MATRIX_ROWS][MATRIX_COLS] = { */
/*     [0] = LAYOUT( */
/*             KC_A, KC_B, KC_C */
/*             ) */
/* }; */


#include QMK_KEYBOARD_H

#define DOUBLE_CLICK_TIME 250

enum custom_keycodes {
    MY_A = SAFE_RANGE,
    MY_B,
    MY_C
};

static uint16_t click_timer;
static uint16_t pending_key = KC_NO;

static uint16_t lowercase_key(uint16_t custom_key) {
    switch (custom_key) {
        case MY_A: return KC_A;
        case MY_B: return KC_B;
        case MY_C: return KC_C;
    }

    return KC_NO;
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
    if (keycode < MY_A || keycode > MY_C)
        return true;

    // We care only about presses, not releases.
    if (!record->event.pressed) {
        return false;
    }

    if (pending_key == keycode &&
        timer_elapsed(click_timer) < DOUBLE_CLICK_TIME) {

        // Second click: uppercase.
        tap_code16(S(keycode == MY_A ? KC_A :
                     keycode == MY_B ? KC_B : KC_C));

        pending_key = KC_NO;
    } else {
        // If another click was waiting, it was a single click.
        if (pending_key != KC_NO)
            tap_code(lowercase_key(pending_key));

        // Start waiting to see whether THIS click gets a partner.
        pending_key = keycode;
        click_timer = timer_read();
    }

    return false;
}

void housekeeping_task_user(void) {
    if (pending_key != KC_NO &&
        timer_elapsed(click_timer) >= DOUBLE_CLICK_TIME) {

        tap_code(lowercase_key(pending_key));
        pending_key = KC_NO;
    }
}

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {
    [0] = LAYOUT(
        MY_A, MY_B, MY_C
    )
};

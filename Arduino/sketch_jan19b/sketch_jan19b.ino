#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <EEPROM.h>


#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
// The pins for I2C are defined by the Wire-library. 
// On an arduino UNO:       A4(SDA), A5(SCL)
// On an arduino MEGA 2560: 20(SDA), 21(SCL)
// On an arduino LEONARDO:   2(SDA),  3(SCL), ...
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

void NewTetro (void);
void TowerInit (void);

#define JOY_CLICK 9
#define JOY_Y A1
#define JOY_X A2

#define BOARD_WIDTH 8
#define BOARD_HEIGHT 16

#define STATE_GAME_SELECT 1
#define STATE_TETRIS_GAMEOVER 2
#define STATE_TETRIS_GAME 3
#define STATE_TOWER_GAME 4


#define GAME_SELECT_RIGHT 5
#define GAME_SELECT_LEFT 6
#define GAME_SELECT_CENTER 7

#define GAME_TETRIS 101
#define GAME_TOWER 102

#define DOWN_QUICK_CYCLE 3
#define DOWN_CYCLE 20
#define DOWN_MIN_CYCLE 5

//completed lines until speeding up 
#define DOWN_CYCLE_ACCELERATION 12

#define HORIZ_CYCLE 5
#define HORIZ_SHORT_CYCLE 2
#define HORIZ_LIGHT 350
#define HORIZ_FULL 450

#define ROTATE_CYCLE 12
#define ROTATE_SHORT_CYCLE 5
#define ROTATE_LIGHT 350
#define ROTATE_FULL 450

//   TOWER DEFINES

//fractions of a pixel used to more exactly place the player to better control player speed
#define TOWER_FRAC 100


#define TOWER_MAX_PLATFORM 4
#define TOWER_LEVEL_DELTA 30
#define TOWER_MAX_VX 10
#define TOWER_VY_JUMP 10
#define TOWER_VY_FALL 3 

struct {
    uint8_t board[BOARD_HEIGHT][BOARD_WIDTH];

    uint8_t state;


    uint8_t game_select_state;
    uint8_t game_select_game;

    int score; 

    int tetris_highscore; 
    int next_tetro;

    uint8_t tetro_type;
    uint8_t tetro_rot;
    uint8_t tetro_cx;
    uint8_t tetro_cy; 

    uint8_t last_push; 

    int8_t x_state;
    int x_timer; 

    int8_t y_state;
    int y_timer;
    union {
        int down_timer;
        int tower_down_timer; 
    };
    int down_cycle; 


    int8_t tower_x0[TOWER_MAX_PLATFORM];
    int8_t tower_x1[TOWER_MAX_PLATFORM];
    uint8_t tower_y[TOWER_MAX_PLATFORM];
    int tower_player_x;
    int tower_player_y;
    int tower_player_x_frac; 
    int tower_player_y_frac; 
    int tower_player_vx;
    int tower_player_vy;
} game; 


#define TETR_S 1
#define TETR_Z 2
#define TETR_I 3
#define TETR_L 4
#define TETR_L2 5
#define TETR_SQ 6
#define TETR_T 7

#define TETRIS_HIGHSCORE_MSB 0
#define TETRIS_HIGHSCORE_LSB 1

int RandTetro (void) {
    int ret = game.next_tetro;
    game.next_tetro = random(1, 8);
    return ret; 
}

void PackXY(int (*xy)[4][2], int x1, int y1, int x2, int y2, int x3, int y3) {
    (*xy)[1][0] = x1;
    (*xy)[1][1] = y1;
    (*xy)[2][0] = x2;
    (*xy)[2][1] = y2;
    (*xy)[3][0] = x3;
    (*xy)[3][1] = y3;
}

void GenerateTetroXY(int type, int rot, int cx, int cy, int (*xy)[4][2]) {
    rot = (4 + (rot % 4)) % 4; 
    (*xy)[0][0] = cx;
    (*xy)[0][1] = cy;

    switch (type) {
    case TETR_S:
        switch (rot % 2) {
        case 0:
//  X   
//  0X
//   X
            PackXY(xy, cx, cy - 1, cx + 1, cy, cx + 1, cy + 1);
            break;
        case 1:
//  0X
// XX
            PackXY(xy, cx + 1, cy, cx - 1, cy + 1, cx, cy + 1);
            break;
        }
        break;
    case TETR_Z:
        switch (rot % 2) {
        case 0:
//   X   
//  0X
//  X
            PackXY(xy, cx + 1, cy - 1, cx + 1, cy, cx, cy + 1);
            break;
        case 1:
// X0
//  XX
            PackXY(xy, cx - 1, cy, cx, cy + 1, cx + 1, cy + 1);
            break;
        }
        break;
    case TETR_SQ:
        PackXY(xy, cx + 1, cy, cx, cy + 1, cx + 1, cy + 1);
        break;
    case TETR_I:
        switch (rot % 2) {
        case 0:
            PackXY(xy, cx, cy - 1, cx, cy + 1, cx, cy + 2);
            break;
        case 1:
            PackXY(xy, cx - 1, cy, cx + 1, cy, cx + 2, cy);
            break;
        }
        break;
    case TETR_L:
        switch (rot) {
        case 0:
// X
// X0X
            PackXY(xy, cx - 1, cy - 1, cx - 1, cy, cx + 1, cy);
            break;
        case 1:
// XX
// 0
// X
            PackXY(xy, cx, cy - 1, cx, cy + 1, cx + 1, cy - 1);
            break;
        case 2:
// X0X
//   X
            PackXY(xy, cx - 1, cy, cx + 1, cy, cx + 1, cy + 1);
            break;
        case 3:
//  X
//  0
// XX
            PackXY(xy, cx, cy - 1, cx - 1, cy + 1, cx, cy + 1);
            break;
        }
        break;
    case TETR_L2:
        switch (rot) {
        case 0:
//   X
// X0X
            PackXY(xy, cx + 1, cy - 1, cx - 1, cy, cx + 1, cy);
            break;
        case 1:
// X
// 0
// XX
            PackXY(xy, cx, cy - 1, cx, cy + 1, cx + 1, cy + 1);
            break;
        case 2:
// X0X
// X

            PackXY(xy, cx - 1, cy, cx + 1, cy, cx - 1, cy + 1);
            break;
        case 3:
// XX
//  0
//  X
            PackXY(xy, cx, cy - 1, cx - 1, cy - 1, cx, cy + 1);
            break;
        }
        break;
    case TETR_T:
        switch (rot) {
        case 0:
//  X
// X0X
            PackXY(xy, cx, cy - 1, cx - 1, cy, cx + 1, cy);
            break;
        case 1:
// X
// 0X
// X
            PackXY(xy, cx, cy - 1, cx, cy + 1, cx + 1, cy);
            break;
        case 2:
// X0X
//  X

            PackXY(xy, cx - 1, cy, cx + 1, cy, cx, cy + 1);
            break;
        case 3:
//  X
// X0
//  X
            PackXY(xy, cx, cy - 1, cx - 1, cy, cx, cy + 1);
            break;
        }
        break;
    }
}

void ResetBoard(uint8_t value = 0) {
    memset(game.board, value, sizeof(game.board));
    game.score = 0; 
    RandTetro ();
}

void ResetGame() {
    Serial.println("game reset");
    ResetBoard ();
    game.state = STATE_GAME_SELECT;
    game.game_select_state = GAME_SELECT_CENTER; 

    game.last_push = 0;
}

void DrawBoard() {
    display.clearDisplay();

    int xy[4][2];

    GenerateTetroXY(game.next_tetro, 0, 0, 0, &xy);

    for (int i=0 ; i<4 ; i++) {
        int col = xy[i][0];
        int row = xy[i][1];
        display.drawRect(20 + row * 4, 8 + col * 4, 4, 4, SSD1306_WHITE);
    }


    display.setRotation (3);
    char c[8];
    sprintf(c, "%d", game.score % 100);
    display.setTextSize(1); // Draw 2X-scale text
    display.setTextColor(SSD1306_WHITE);
    display.setCursor(2, 16);
    display.println(c);

    display.setTextSize(1); // Draw 2X-scale text
    display.setCursor(6, 105);
    display.println("Hi:");

    sprintf(c, "%d", game.tetris_highscore);
    display.setTextSize(1); // Draw 2X-scale text
    display.setCursor(4, 115);
    display.println(c);

    display.setRotation (0);

    for (int col=0 ; col<BOARD_WIDTH ; ++col) {
        for (int row=0 ; row<BOARD_HEIGHT ; ++row) {
            if (game.board[row][col]) {
                display.drawRect(32 + row * 4, col * 4, 4, 4, SSD1306_WHITE);
            }
        }
    } 
    display.drawRect(31 + BOARD_HEIGHT * 4 + 1, 0, 1, 32, SSD1306_WHITE);
    display.drawRect(31, 0, 1, 32, SSD1306_WHITE);
    display.display();
}

void GameSelectTick(int x, int push) {
    if (game.state != STATE_GAME_SELECT)  {
        return;
    }

    if (push) {
        game.last_push = 1; 
    } else {
        if (game.last_push) {
            switch(game.game_select_game) {
            case GAME_TETRIS:
                Serial.print("starting tetris");
                game.state = STATE_TETRIS_GAME; 
                ResetBoard();
                NewTetro ();
                return; 
            case GAME_TOWER:
                TowerInit (); 
                return;
            default:
                Serial.print("illegal game");
            }
        }
    }

    if (200 > abs(x)) { //joystick neutral
        game.game_select_state = GAME_SELECT_CENTER;
    } else if (game.game_select_state == GAME_SELECT_CENTER && x > 400) { // rotating games
        game.game_select_game = (game.game_select_game == GAME_TETRIS) ? GAME_TOWER : GAME_TETRIS;
        game.game_select_state = GAME_SELECT_LEFT;
        Serial.print("select left");
    } else if (game.game_select_state == GAME_SELECT_CENTER && x < -400) { // rotating games
        game.game_select_game = (game.game_select_game == GAME_TETRIS) ? GAME_TOWER : GAME_TETRIS;
        game.game_select_state = GAME_SELECT_RIGHT;
        Serial.print("select right");
    } 



    display.clearDisplay();
    display.setTextSize(2); // Draw 2X-scale text
    display.setTextColor(SSD1306_WHITE);
    char *txt = game.game_select_game == GAME_TETRIS ? "TETRIS" : "TOWER";
    display.setCursor(65 - strlen(txt) * 6, 12);
    display.println(txt);
    display.display();      // Show initial text
}

int XYCheck(int (*xy)[4][2]) {
    for (int i=0 ; i<4 ; ++i) {
        int x = (*xy)[i][0]; 
        int y = (*xy)[i][1]; 
        if (x < 0 || x >= BOARD_WIDTH || x < 0 || y >= BOARD_HEIGHT) {
            return 0; 
        }
        if (game.board[y][x] != 0) {
            return 0; 
        }
    }
    return 1; 
}

void StampTetro(int (*xy)[4][2], uint8_t value) {
    Serial.print("stamping ");

    Serial.print(value);
    Serial.print(" at ");
    for (int i=0 ; i<4 ; ++i) {
        int x = (*xy)[i][0];
        int y = (*xy)[i][1];
        Serial.print(x);
        Serial.print(":");
        Serial.print(y);
        Serial.print(" ");
        if (x >= 0 && x < BOARD_WIDTH && y >= 0 && y < BOARD_HEIGHT) {
            game.board[y][x] = value;
        }
    }
    Serial.println("");
}

int TetroSpawnY(int type) {
    switch(type) {
    case TETR_S:
    case TETR_Z:
    case TETR_I:
    case TETR_L:
    case TETR_L2:
    case TETR_T:
        return 1;
    case TETR_SQ:
        return 0;
    }
}

void NewTetro (void) {
    int type = RandTetro();

    int cx = 3, cy = TetroSpawnY(type);
    int xy[4][2];
    GenerateTetroXY(type, 0, cx, cy, &xy);

    if (XYCheck(&xy)) {
        game.tetro_type = type;
        game.tetro_rot = 0;
        game.tetro_cx = cx;
        game.tetro_cy = cy; 
        game.state = STATE_TETRIS_GAME;

        game.down_cycle = DOWN_CYCLE;
        for (int i=0 ; i<(game.score / DOWN_CYCLE_ACCELERATION); ++i) {
            game.down_cycle = game.down_cycle * 4 / 5; 
        }
        if (game.down_cycle < DOWN_MIN_CYCLE) {
            game.down_cycle = DOWN_MIN_CYCLE;
        }
        game.down_timer = game.down_cycle; 

        StampTetro(&xy, 1);
    } else {
        if (game.score > game.tetris_highscore) {
            game.tetris_highscore = game.score;
            EEPROM.write(TETRIS_HIGHSCORE_MSB, game.score / 100);
            EEPROM.write(TETRIS_HIGHSCORE_LSB, game.score % 100);  
        }
        ResetBoard(1);
        DrawBoard(); 
        game.state = STATE_TETRIS_GAMEOVER; 
        game.last_push = 0; 
    }
}

// the setup function runs once when you press reset or power the board
void setup() {
    Serial.begin(9600);           // set up Serial library at 9600 bps
    Serial.print("initializing random seed: ");
    long seed = analogRead(0);

    Serial.println(seed);
    randomSeed(seed);

    pinMode(JOY_CLICK, INPUT_PULLUP);
    pinMode(JOY_X, INPUT_PULLUP);
    pinMode(JOY_Y, INPUT_PULLUP);  

    ResetGame();
    game.game_select_game = GAME_TETRIS;

// display

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  // Clear the buffer
  display.clearDisplay();
  display.display();

//  EEPROM.write(TETRIS_HIGHSCORE_MSB, 0);
//  EEPROM.write(TETRIS_HIGHSCORE_LSB, 0);  

  game.tetris_highscore = (int)EEPROM.read(TETRIS_HIGHSCORE_MSB) * 100 + EEPROM.read(TETRIS_HIGHSCORE_LSB);
}

void Rotate(int delta) {
    int xyold[4][2];
    int xynew[4][2];

    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xyold);
    StampTetro(&xyold, 0);

    game.tetro_rot += delta;
    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xynew);
    
    if (XYCheck(&xynew)) {
        StampTetro(&xynew, 1);
    } else {
        GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx + 1, game.tetro_cy, &xynew);            
        if (XYCheck(&xynew)) {
            game.tetro_cx += 1;
            StampTetro(&xynew, 1);
            return;
        }
        GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx - 1, game.tetro_cy, &xynew);
        if (XYCheck(&xynew)) {
            game.tetro_cx -= 1;
            StampTetro(&xynew, 1);
            return;
        }
        game.tetro_rot -= delta;
        StampTetro(&xyold, 1);
    }
}


void Horiz(int delta) {
    int xyold[4][2];
    int xynew[4][2];

    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xyold);
    StampTetro(&xyold, 0);

    game.tetro_cx += delta;
    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xynew);
    
    if (XYCheck(&xynew)) {
        StampTetro(&xynew, 1);
    } else {
        game.tetro_cx -= delta;
        StampTetro(&xyold, 1);
    }
}

void XTick(int x) {
    if (abs(x) < HORIZ_LIGHT && game.x_state != 0) {
        game.x_state = 0;
        Serial.println("X NULL");
        return;
    }
    if (x >= HORIZ_FULL && game.x_state < 1) {
        Serial.println("RIGHT");
        Horiz(1);

        game.x_state = 1;
        game.x_timer = HORIZ_CYCLE; 
        return; 
    }
    if (x <= -HORIZ_FULL && game.x_state > -1) {
        Serial.print(game.x_state);
        Serial.println("LEFT");
        Horiz(-1);
        game.x_state = -1;
        game.x_timer = HORIZ_CYCLE; 
        return; 
    }

    game.x_timer--; 
    if (x > HORIZ_FULL && game.x_state >= 1 && game.x_timer <= 0) {
        game.x_state = 2;
        Serial.println("RIGHT repeatable");
        Horiz(1);
        game.x_timer = HORIZ_SHORT_CYCLE;
        return;
    }
    if (x < -HORIZ_FULL && game.x_state <= -1 && game.x_timer <= 0) {
        game.x_state = -2;
        Serial.println("LEFT repeatable");
        Horiz(-1);
        game.x_timer = HORIZ_SHORT_CYCLE;
        return;
    }
}

void RotateTick(int y) {
    if (abs(y) < ROTATE_LIGHT && game.y_state != 0) {
        game.y_state = 0;
        return;
    }
    if (y >= ROTATE_FULL && game.y_state < 1) {
        Rotate(1);

        game.y_state = 1;
        game.y_timer = ROTATE_CYCLE; 
        return; 
    }
    if (y <= -ROTATE_FULL && game.y_state > -1) {
        Rotate(-1);
        game.y_state = -1;
        game.y_timer = ROTATE_CYCLE; 
        return; 
    }

    game.y_timer--; 
    if (y > ROTATE_FULL && game.y_state >= 1 && game.y_timer <= 0) {
        game.y_state = 2;
        Rotate(1);
        game.y_timer = ROTATE_SHORT_CYCLE;
        return;
    }
    if (y < -ROTATE_FULL && game.y_state <= -1 && game.y_timer <= 0) {
        game.y_state = -2;
        Rotate(-1);
        game.y_timer = ROTATE_SHORT_CYCLE;
        return;
    }
}

void DeleteFullLines() {
    for (int y=BOARD_HEIGHT-1 ; y>=0 ; --y) {
        int count = 0; 
        for (int x=0 ; x<BOARD_WIDTH ; ++x) {
            count += game.board[y][x];
        }
        if (count == BOARD_WIDTH) {
            for (int y2=y ; y2>0 ; --y2) {
                for (int x=0 ; x<BOARD_WIDTH ; ++x) {
                    game.board[y2][x] = game.board[y2 - 1][x];
                }
            }
            for (int x=0 ; x<BOARD_WIDTH ; ++x) {
                game.board[0][x] = 0; 
            }
            ++y;
            game.score++; 
        }
    }
}

void DownTick(int push) {
    int xyold[4][2];
    int xynew[4][2];

    if (!push && game.down_timer > DOWN_QUICK_CYCLE) {
        game.down_timer = DOWN_QUICK_CYCLE;
    }
    
    if (--game.down_timer > 0) {
        return;
    }
    game.down_timer = game.down_cycle;

    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xyold);
    StampTetro(&xyold, 0);

    game.tetro_cy += 1;
    GenerateTetroXY(game.tetro_type, game.tetro_rot, game.tetro_cx, game.tetro_cy, &xynew);
    
    if (XYCheck(&xynew)) {
        StampTetro(&xynew, 1);
    } else {
        game.tetro_cy -= 1;
        StampTetro(&xyold, 1);
        DeleteFullLines();
        NewTetro ();
    }
}

/// TOWER GAME


void TowerNewLevel(void) {
    for (int i=TOWER_MAX_PLATFORM-1 ; i>0 ; --i) {
        game.tower_y[i] = game.tower_y[i - 1];
        game.tower_x0[i] = game.tower_x0[i - 1];
        game.tower_x1[i] = game.tower_x1[i - 1];
    }
    game.tower_y[0] = 0;
    game.tower_x0[0] = random(0, SCREEN_HEIGHT - 5);
    game.tower_x1[0] = random(game.tower_x0[0] + 5, SCREEN_HEIGHT);
}

void TowerScroll(int dy) {
    for (int i=0 ; i<TOWER_MAX_PLATFORM ; ++i) {
        game.tower_y[i] += dy;
    }
    if (game.tower_y[0] >= TOWER_LEVEL_DELTA) {
        TowerNewLevel();
    }
}

void TowerInit (void) {
    game.state = STATE_TOWER_GAME;
    game.last_push = 0;
    for (int i=0 ; i<TOWER_MAX_PLATFORM ; ++i) {
        TowerScroll(TOWER_LEVEL_DELTA);
    }
}

void DrawTower (void) {
    display.clearDisplay();

    for (int i=0 ; i<TOWER_MAX_PLATFORM ; ++i) {
//        if (game.tower_y[i] < SCREEN_WIDTH) {
            int x0 = game.tower_x0[i];
            int x1 = game.tower_x1[i];
            display.drawRect(game.tower_y[i], x0, 3, x1 - x0 + 1, SSD1306_WHITE);
//        }
    }
    display.display();
}

void TowerTick(int x, int y, int push) {
    if (!push && game.last_push) {
        game.state = STATE_GAME_SELECT; 
        game.last_push = 0; 
    }
    game.last_push = push; 

    TowerScroll(1);
    DrawTower ();

    for (int i=0 ; i<TOWER_MAX_PLATFORM ; ++i) {
        Serial.print(game.tower_y[i]);
        Serial.print(" ");
    }
    Serial.println(".");
}

// the loop function runs over and over again forever
void loop() {
    long analogX, analogY, push;  
  
    analogY = (long)analogRead(JOY_X) - 512; // reversed for personal convenience
    analogX = (long)analogRead(JOY_Y) - 512; 
    push = digitalRead(JOY_CLICK);

    switch (game.state) {
    case STATE_GAME_SELECT:
        GameSelectTick(analogX, push);
        break;
    case STATE_TETRIS_GAME:
        XTick(analogX);
        RotateTick(analogY);
        DownTick(push);
        DrawBoard();
        delay(20);
        break;
    case STATE_TOWER_GAME:
        TowerTick(analogX, analogY, push);
        break;
    case STATE_TETRIS_GAMEOVER:
        if (!push) {
            if (game.last_push) {
                ResetGame();
            }
        } else {
            game.last_push = 1; 
        }
        break;
    }
}



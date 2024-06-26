/**The MIT License (MIT)

Copyright (c) 2016 by Rene-Martin Tudyka
Based on the SSD1306 OLED library Copyright (c) 2015 by Daniel Eichhorn (http://blog.squix.ch),
available at https://github.com/squix78/esp8266-oled-ssd1306

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

See more at http://blog.squix.ch
*/
#include <Wire.h>
#include <SPI.h>
#include "SH1106.h"
#include "SH1106Ui.h"
#include "images.h"

#include <ESP8266WiFi.h>

// Pin definitions for I2C
//#define OLED_SDA    D2  // pin 14
//#define OLED_SDC    D4  // pin 12
//#define OLED_ADDR   0x3C

/* Hardware Wemos D1 mini SPI pins
 D5 GPIO14   CLK         - D0 pin OLED display
 D6 GPIO12   MISO (DIN)  - not connected
 D7 GPIO13   MOSI (DOUT) - D1 pin OLED display
 D1 GPIO5    RST         - RST pin OLED display
 D2 GPIO4    DC          - DC pin OLED
 D8 GPIO15   CS / SS     - CS pin OLED display
*/

// Pin definitions for SPI
// ESP8266
//#define OLED_RESET  5   // RESET
//#define OLED_DC     4   // Data/Command
//#define OLED_CS     15  // Chip select
// Node MCU
#define OLED_RESET  D1   // RESET
#define OLED_DC     D2   // Data/Command
#define OLED_CS     D8   // Chip select

// Uncomment one of the following based on OLED type
SH1106 display(true, OLED_RESET, OLED_DC, OLED_CS); // FOR SPI
//SH1106   display(OLED_ADDR, OLED_SDA, OLED_SDC);    // For I2C
SH1106Ui ui     ( &display );

String IpAddress2String(const IPAddress& ipAddress) {
    return String(ipAddress[0]) + String(".") +\
        String(ipAddress[1]) + String(".") +\
        String(ipAddress[2]) + String(".") +\
        String(ipAddress[3])  ; 
}

bool msOverlay(SH1106 *display, SH1106UiState* state) {
    display->setTextAlignment(TEXT_ALIGN_RIGHT);
    display->setFont(ArialMT_Plain_10);
    display->drawString(128, 0, IpAddress2String(WiFi.localIP()));
    return true;
}

bool drawFrame1(SH1106 *display, SH1106UiState* state, int x, int y) {
  // draw an xbm image.
  // Please note that everything that should be transitioned
  // needs to be drawn relative to x and y

  // if this frame need to be refreshed at the targetFPS you need to
  // return true
  display->drawXbm(x + 34, y + 14, WiFi_Logo_width, WiFi_Logo_height, WiFi_Logo_bits);
  return false;
}

bool drawFrame2(SH1106 *display, SH1106UiState* state, int x, int y) {
  // Demonstrates the 3 included default sizes. The fonts come from SH1106Fonts.h file
  // Besides the default fonts there will be a program to convert TrueType fonts into this format
  display->setTextAlignment(TEXT_ALIGN_LEFT);
  display->setFont(ArialMT_Plain_10);
  display->drawString(0 + x, 10 + y, "Arial 10");

  display->setFont(ArialMT_Plain_16);
  display->drawString(0 + x, 20 + y, "Arial 16");

  display->setFont(ArialMT_Plain_24);
  display->drawString(0 + x, 34 + y, "Arial 24");

  return false;
}

bool drawFrame3(SH1106 *display, SH1106UiState* state, int x, int y) {
  // Text alignment demo
  display->setFont(ArialMT_Plain_10);

  // The coordinates define the left starting point of the text
  display->setTextAlignment(TEXT_ALIGN_LEFT);
  display->drawString(0 + x, 11 + y, "Left aligned (0,10)");

  // The coordinates define the center of the text
  display->setTextAlignment(TEXT_ALIGN_CENTER);
  display->drawString(64 + x, 22, "Center aligned (64,22)");

  // The coordinates define the right end of the text
  display->setTextAlignment(TEXT_ALIGN_RIGHT);
  display->drawString(128 + x, 33, "Right aligned (128,33)");
  return false;
}

WiFiClient client;
char txt[200]  = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore.";
int txt_idx = 0; 

bool drawFrame4(SH1106 *display, SH1106UiState* state, int x, int y) {
  // Demo for drawStringMaxWidth:
  // with the third parameter you can define the width after which words will be wrapped.
  // Currently only spaces and "-" are allowed for wrapping
  display->setTextAlignment(TEXT_ALIGN_LEFT);
  display->setFont(ArialMT_Plain_10);

  display->drawStringMaxWidth(0 + x, 10 + y, 128, txt);
  return false;
}

// how many frames are there?
int frameCount = 4;
// this array keeps function pointers to all frames
// frames are the single views that slide from right to left
bool (*frames[])(SH1106 *display, SH1106UiState* state, int x, int y) = { drawFrame1, drawFrame2, drawFrame3, drawFrame4 };

bool (*overlays[])(SH1106 *display, SH1106UiState* state)             = { msOverlay };
int overlaysCount = 1;

void setup() {
    delay(10);

    Serial.begin(9600);
    Serial.println("connecting");

    WiFi.begin("DIGI-77CA", "QqiD8937");
    while (WiFi.status() != WL_CONNECTED) {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("I'm In!!!");


    if (client.connect("192.168.100.2", 8000)) {
        Serial.println("connected to server");
        client.println("GET /a.txt HTTP/1.1");
        client.println("Host: 192.168.100.2");
        client.println("Connection: close");
        client.println();
    }



    ui.setTargetFPS(30);

    ui.setActiveSymbole(activeSymbole);
    ui.setInactiveSymbole(inactiveSymbole);

    // You can change this to
    // TOP, LEFT, BOTTOM, RIGHT
    ui.setIndicatorPosition(BOTTOM);

    // Defines where the first frame is located in the bar.
    ui.setIndicatorDirection(LEFT_RIGHT);

    // You can change the transition that is used
    // SLIDE_LEFT, SLIDE_RIGHT, SLIDE_TOP, SLIDE_DOWN
    ui.setFrameAnimation(SLIDE_LEFT);

    // Add frames
    ui.setFrames(frames, frameCount);

    // Add overlays
    ui.setOverlays(overlays, overlaysCount);

    // Inital UI takes care of initalising the display too.
    ui.init();

    display.flipScreenVertically();

}

void loop() {
    int remainingTimeBudget = ui.update();

    while (client.available()) {
        char c = client.read();
        if ((int) c != 13) {
            Serial.write(c);
            if (txt_idx == 0 && c == 10) {
                continue;
            }
            if (txt_idx < (sizeof(txt) - 2)) {
                txt[txt_idx++] = c;
                txt[txt_idx] = 0;
            }
        } else {
            txt_idx = 0; 
        }
    }
    if (remainingTimeBudget > 0) {
        // You can do some work here
        // Don't do stuff if you are below your
        // time budget.
        delay(remainingTimeBudget);
    }
}

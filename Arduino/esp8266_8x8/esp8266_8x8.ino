
#define DIN D0
#define CS D1
#define CLK D2

// MAX7219 Control registers

#define DECODE_MODE     9
#define INTENSITY    0x0A
#define SCAN_LIMIT   0x0B
#define SHUTDOWN     0x0C
#define DISPLAY_TEST 0x0F


void sendByte(uint8_t val) {
  for (int i = 128 ; i > 0 ; i >>= 1) {
    digitalWrite(CLK, LOW);
    digitalWrite(DIN, (i & val) ? HIGH : LOW);
    delay(1);
    digitalWrite(CLK, HIGH);
    delay(1);
  }
}

void sendData(uint8_t address, uint8_t val) {
  digitalWrite(CS, LOW);
  sendByte(address);
  sendByte(val);
  digitalWrite(CS, HIGH);
}


void setup() {
  // put your setup code here, to run once:
  pinMode(CS, OUTPUT);
  pinMode(DIN, OUTPUT);
  pinMode(CLK, OUTPUT);
  
  sendData(DISPLAY_TEST, 0);
  sendData(INTENSITY, 1);
  sendData(SCAN_LIMIT, 0x0f); // "scan all digits"
  sendData(DECODE_MODE, 0); //bcd mode no ty
  sendData(SHUTDOWN, 1);
}


int x=0, y=0;

void loop() {
  for (int i = 0 ; i<8 ; ++i) {
    if (i == y) {
      sendData(i + 1, 1 << x);
    } else {
      sendData(i + 1, 0);
    }
  }

  x += 1;
  if (x == 8) {
    y += 1;
    x = 0;
    if (y == 8) {
      y = 0;
    }
  }
}

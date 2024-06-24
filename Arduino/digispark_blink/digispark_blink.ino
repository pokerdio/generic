
void w(int val) {
  digitalWrite(0, val);
  digitalWrite(1, val);
}

void setup() {
  // put your setup code here, to run once:
  pinMode(0, OUTPUT);
  pinMode(1, OUTPUT);  
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0 ; i<6 ; ++i) {
  w(HIGH);
  delay(70);
  w(LOW);
  delay(30);

  w(HIGH);
  delay(70);
  w(LOW);
  delay(130);
  }
  delay(500);
}

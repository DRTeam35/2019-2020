void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int data = random(0, 1000);

  Serial.print("data=");
  Serial.println(data);

  delay(2500);
/*if(Serial.available()>0){
    int incoming = Serial.read();
    Serial.print("character recieved: ");
    Serial.print(incoming, DEC);
  } */

}

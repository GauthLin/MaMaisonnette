#include <Wire.h>

void setup() {
  Serial.begin(115200);
  
  Wire.begin(0x08);
  Wire.onRequest(requestEvent);

  Serial.println("Setiup finished");
}

void loop() {
  // put your main code here, to run repeatedly:

}

/*
 *  Envoi de données à la RPi maître par l'I2C lorsqu'une communication est établie
 */
void requestEvent() 
{
  int tempA = analogRead(0);
  int tempB = analogRead(1);
  int tempC = analogRead(2);
  int tempD = analogRead(3);
  
  // construction du paquet de 8 bytes à envoyer
  byte regs[] = 
  {
    tempA >> 8,
    tempA,
    tempB >> 8,
    tempB,
    tempC >> 8,
    tempC,
    tempD >> 8,
    tempD
  };
  Wire.write(regs, 8);
  Serial.println("Température A:" + tempA);
  Serial.println("Température B:" + tempB);
  Serial.println("Température C:" + tempC);
  Serial.println("Température D:" + tempD);
}

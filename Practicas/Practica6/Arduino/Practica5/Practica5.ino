int sensor = A0;
int leds[4] = {8, 9, 10, 11};

void setup()
{
  Serial.begin(9600);
  Serial.setTimeout(10);
  for(int i = 0; i < 4; i++)
  {
    pinMode(leds[i], OUTPUT);
  }
}

int lecturas[30] = {};
int average = 0;
// long currentMillis, previousMillis = 0;
// long interval = 1000;  //10 segundos
void loop()
{
  if (Serial.available() > 0)
  {
    int ledPos = Serial.parseInt();
    for (int i = 0; i < 4; i++)
    {
      digitalWrite(leds[i], LOW);
    }
    digitalWrite(leds[ledPos], HIGH);
  }

  for(int i = 0; i < 30; i++)
  {
    lecturas[i] = analogRead(sensor);
    delay(10);
  }

  average = 0;
  for(int i = 0; i < 30; i++)
  {
    average += lecturas[i];
  }

  average /= 30;

  Serial.println(average);
  delay(500);
}

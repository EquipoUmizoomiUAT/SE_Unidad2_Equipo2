const int photoresistor = A0;
const int lm35 = A1;

void setup() {
  Serial.begin(9600);
}

const int totalReadings = 30;
int lightIntensity[totalReadings];
int avgLight;
int temperature[totalReadings];
int avgTemp;

unsigned long previousMillis = 0;
const long interval = 300000; // 5 minutes in milliseconds

void loop() {
  unsigned long currentMillis = millis();

  if (currentMillis - previousMillis >= interval)
  {
    previousMillis = currentMillis;

    for (int i = 0; i < totalReadings; i++)
    {
      lightIntensity[i] = analogRead(photoresistor);
      temperature[i] = analogRead(lm35);
      delayMicroseconds(100);
    }

    avgLight = 0;
    avgTemp = 0;
    for (int i = 0; i < totalReadings; i++)
    {
      avgLight += lightIntensity[i];
      avgTemp += temperature[i];
    }

    avgLight /= totalReadings;
    avgTemp /= totalReadings;

    Serial.print(avgLight);
    Serial.print(",");
    Serial.println(avgTemp);
  }
}
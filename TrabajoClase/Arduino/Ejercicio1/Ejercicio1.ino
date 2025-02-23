int sensor = A0;

void setup()
{
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];

void loop()
{ 
  for(int i = 0; i < totalLecturas; i++)
  {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  int prom = 0;
  for(int i = 0; i < totalLecturas; i++)
  {
    prom += valor[i];
  }
  prom /= totalLecturas;
  Serial.println(prom);
  delay(10);
}
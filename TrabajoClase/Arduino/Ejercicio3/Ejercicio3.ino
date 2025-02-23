int sensor = A0;

void start()
{
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];
int valorMayor = -1;

void loop()
{
  for(int i = 0; i < totalLecturas; i++)
  {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  valorMayor = -1;
  for(int i = 0; i < totalLecturas; i++)
  {
    if(valor[i] > valorMayor)
    {
      valorMayor = valor[i]
    }
  }
  Serial.println(valorMayor);
  delay(10);
}
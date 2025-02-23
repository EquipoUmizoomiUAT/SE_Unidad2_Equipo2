int sensor = A0;

void start()
{
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];
int valorMenor = 1024;  // En Arduino las lecturas analogicas tienen un valor maximo de 1023
                        // El valor menor no resulta factible en casos donde una lectura pequeña pueda afectar demasiado al sistema

void loop()
{
  for(int i = 0; i < totalLecturas; i++)
  {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  valorMenor = 1024;
  for(int i = 0; i < totalLecturas; i++)
  {
    if(valor[i] < valorMenor)
    {
      valorMenor = valor[i]
    }
  }
  Serial.println(valorMenor);
  delay(10);
}
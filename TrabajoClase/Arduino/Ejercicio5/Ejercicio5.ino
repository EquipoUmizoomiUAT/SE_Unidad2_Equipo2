int sensor = A0;

void setup()
{
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[30];
int moda, frecuenciaMaxima, frecuenciaActual;

void loop()
{
  for(int i = 0; i < totalLecturas; i++)
  {
    valor[i] = analogRead(sensor);
    delayMicroseconds(100);
  }

  // Ordeno el vector
  for(int i = 0; i < totalLecturas; i++)
  {
    for(int j = i + 1; j < totalLecturas - 1; j++)
    {
      if(valor[j] < valor[i])
      {
        int temp = valor[i];
        valor[i] = valor[j];
        valor[j] = temp;
      }
    }
  }

  moda = valor[0];
  frecuenciaMaxima = 1;
  frecuenciaActual = 1;
  // Recorro el arreglo a partir del segundo valor
  for(int i = 1; i < totalLecturas; i++)
  {
    if (valor[i] == valor[i - 1])
    {
      // Si es el mismo valor que el anterior aumentar la frecuencia de este
      frecuenciaActual++;
    }
    else
    {
      // En caso de que haya un cambio, ver si el valor anterior tubo mayor frecuencia
      if (frecuenciaActual > frecuenciaMaxima)
      {
        // Si es el caso, actualizar valores
        moda = valor[i - 1];
        frecuenciaMaxima = frecuenciaActual;
      }
      frecuenciaActual = 1;
    }
  }
  // En caso de que el ultimo valor sea igual que el penultimo entonces no se entrara al else y no se verificara si 
  //    este numero tiene mayor frecuencia que uno anterior
  if (valor[totalLecturas - 1] == valor[totalLecturas - 2] && frecuenciaActual > frecuenciaMaxima)
  {
    moda = valor[totalLecturas - 1];
  }
  Serial.println(moda);
  delay(10);
}
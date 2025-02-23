int sensors[6] = {A0, A1, A2, A3, A4, A5};
const int totalLecturas = 30;
int lecturaPines[6][totalLecturas];

int getUltimoValor(int arr[])
{
  return arr[totalLecturas - 1];
}

int getPromedio(int arr[])
{
  int promedio = 0;
  for(int i = 0; i < totalLecturas; i++)
  {
    promedio += arr[i];
  }
  return (float)promedio / totalLecturas;
}

int getMediana(int arr[])
{
  for(int i = 0; i < totalLecturas; i++)
  {
    for(int j = i + 1; j < totalLecturas; j++)
    {
      if(arr[j] < arr[i])
      {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
      }
    }
  }
  return arr[totalLecturas / 2];
}

int getModa(int arr[])
{
  int moda = arr[0];
  int frecuenciaMaxima = 1;
  int frecuenciaActual = 1;
  for(int i = 1; i < totalLecturas; i++)
  {
    if (arr[i] == arr[i - 1])
    {
      frecuenciaActual++;
    }
    else
    {
      if (frecuenciaActual > frecuenciaMaxima)
      {
        moda = arr[i - 1];
        frecuenciaMaxima = frecuenciaActual;
      }
      frecuenciaActual = 1;
    }
  }
  if (arr[totalLecturas - 1] == arr[totalLecturas - 2] && frecuenciaActual > frecuenciaMaxima)
  {
    moda = arr[totalLecturas - 1];
  }
  return moda;
}

int getValorMenor(int arr[])
{
  int menor = 1024;
  for(int i = 0; i < totalLecturas; i++)
  {
    if (arr[i] < menor)
    {
      menor = arr[i];
    }
  }
  return menor;
}

int getValorMayor(int arr[])
{
  int mayor = -1;
  for(int i = 0; i < totalLecturas; i++)
  {
    if (arr[i] > mayor)
    {
      mayor = arr[i];
    }
  }
  return mayor;
}

void setup()
{
  Serial.begin(9600);
}

int ultimosValores[6];
float promedios[6];
int modas[6];
int medianas[6];
int mayores[6];
int minimos[6];

void loop()
{
  for (int i = 0; i < 6; i++)
  {
    for (int j = 0; j < totalLecturas; j++)
    {
      lecturaPines[i][j] = analogRead(sensors[i]);
    }
  }

  for (int i = 0; i < 6; i++)
  {
    ultimosValores[i] = getUltimoValor(lecturaPines[i]);
    promedios[i] = getPromedio(lecturaPines[i]);
    modas[i] = getModa(lecturaPines[i]);
    medianas[i] = getMediana(lecturaPines[i]);
    mayores[i] = getValorMayor(lecturaPines[i]);
    minimos[i] = getValorMenor(lecturaPines[i]);
  }

  Serial.print("{");
  for (int i = 0; i < 6; i++) {
    Serial.print("\"Pin ");
    Serial.print(i);
    Serial.print("\": {");
    Serial.print("\"Last Value\": ");
    Serial.print(ultimosValores[i]);
    Serial.print(", \"Average\": ");
    Serial.print(promedios[i]);
    Serial.print(", \"Median\": ");
    Serial.print(medianas[i]);
    Serial.print(", \"Max\": ");
    Serial.print(mayores[i]);
    Serial.print(", \"Min\": ");
    Serial.print(minimos[i]);
    Serial.print(", \"Mode\": ");
    Serial.print(modas[i]);
    Serial.print("}");
    if (i < 5) {
      Serial.print(", ");
    }
  }
  Serial.println("}");
  
  delay(1000);
}
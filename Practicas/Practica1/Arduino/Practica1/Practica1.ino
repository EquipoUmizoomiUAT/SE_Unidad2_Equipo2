int sensor[6] = {A0, A1, A2, A3, A4, A5};

void setup()
{
  Serial.begin(9600);
}

int totalLecturas = 30;
int valor[6][30];
int promedio, valorMayor, valorMenor, mediana;

void loop()
{
  // Para el potenciometro i
  for(int i = 0; i < 4; i++)
  {
    // Obten 30 lecturas
    for(int j = 0; j < totalLecturas; j++)
    {
      // Guarda el valor de la lectura j del potenciometro i
      valor[i][j] = analogRead(sensor[i]);
      delayMicroseconds(100);
    }
  }

  // Ordeno el cuarto vector para sacar la mediana
  for(int i = 0; i < totalLecturas; i++)
  {
    for(int j = i + 1; j < totalLecturas - 1; j++)
    {
      if(valor[3][j] < valor[3][i])
      {
        int temp = valor[3][i];
        valor[3][i] = valor[3][j];
        valor[3][j] = temp;
      }
    }
  }
  //Obtengo el valor de enmedio
  mediana = valor[3][totalLecturas / 2];

  // Proporngo el primer valor del segundo y tercer vector como Mayor y Menor
  // Recorro ambos vectores y busco el valor mayor y menor respectivamente
  valorMayor = valor[1][0];
  valorMenor = valor[2][0];
  for(int i = 0; i < totalLecturas; i++)
  {
    if(valor[2][i] > valorMayor)
    {
      valorMayor = valor[2][i];
    }
    if(valor[1][i] < valorMenor)
    {
      valorMenor = valor[1][i];
    }
  }

  // Inicializo la suma en 0 y sumo los valores del vector
  promedio = 0;
  for(int i = 0; i < totalLecturas; i++)
  {
    promedio += valor[0][i];
  }
  // Saco promedio
  promedio /= totalLecturas;

  // Formato para lectura en python N,N,N,N
  Serial.println(String(promedio) + "," + String(valorMenor) + "," + String(valorMayor) + "," + String(mediana));

  delay(10);
}
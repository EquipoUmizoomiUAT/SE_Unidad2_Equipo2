import math

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from Practicas.Utils import LinealInterpolation, SES
import os


if __name__ == '__main__':
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.width', 1000)
    pd.set_option('display.colheader_justify', 'center')

    readingNumber = '3'

    # Obtiene el directorio del script TratarDatos.py
    currentPath = os.path.dirname(os.path.abspath(__file__))

    # Sube un nivel (a Unidad2)
    practicasPath = os.path.dirname(currentPath)

    # Construye la ruta a Archivo.csv
    filePath = os.path.join(practicasPath, 'Practica2', 'Python', f'sensor_readings{readingNumber}.csv')
    print(filePath)


    plotCheck = 1
    dataset = pd.read_csv(filePath)

    # Check each line for any missing value
    missingValues = dataset.isnull().any(axis=1)
    # Get all the lines with missing values
    incompleteReadings = dataset[missingValues]
    # Print if there is no missing values or if they are, print the missing values
    if incompleteReadings.empty:
        print('Full dataset')
    else:
        exit('Victor del futuro, implementa la interpolacion lineal')

    lightIntensity = dataset['LightIntensity'].sort_values(ascending=True)
    temperature = dataset['Temperature'].sort_values(ascending=True)

    bxData = [lightIntensity, temperature]
    plt.boxplot(bxData, tick_labels=['Light Intensity', 'Temperature'])
    plt.title("Intensidad Luminosa - Temperatura")
    plt.show()

    posQ1 = (len(lightIntensity) - 1) / 4 + 1
    posQ3 = 3 * (len(lightIntensity) - 1) / 4 + 1

    decimal, integer = math.modf(posQ1)
    integer = int(integer)
    lightQ1 = lightIntensity.iloc[integer - 1] + decimal * (lightIntensity.iloc[integer] - lightIntensity.iloc[integer - 1])
    tempQ1 = temperature.iloc[integer - 1] + decimal * (lightIntensity.iloc[integer] - lightIntensity.iloc[integer - 1])

    decimal, integer = math.modf(posQ3)
    integer = int(integer)
    lightQ3 = lightIntensity.iloc[integer - 1] + decimal * (lightIntensity.iloc[integer] - lightIntensity.iloc[integer - 1])
    tempQ3 = temperature.iloc[integer - 1] + decimal * (lightIntensity.iloc[integer] - lightIntensity.iloc[integer - 1])

    lightIQR = lightQ3 - lightQ1

    tolerance = 1.5
    lightLowerLimit = lightIQR - tolerance * lightIQR
    lightUpperLimit = lightIQR + tolerance * lightIQR
    tempLowerLimit = tempQ3 - tolerance * tempQ3
    tempUpperLimit = tempQ3 + tolerance * tempQ3

    lightIntensity = lightIntensity.sort_index(ascending=True)
    temperature = temperature.sort_index(ascending=True)

    lightExport = []
    temperatureExport = []

    for index, value in lightIntensity.items():
        if value < lightLowerLimit or value > lightUpperLimit:
            print(f'Light Outlier: {value}')
            if index == 0:
                lightIntensity[index] = lightIntensity[index + 1]
            elif index == len(lightIntensity) - 1:
                lightIntensity[index] = lightIntensity[index - 1]
            else:
                newValue = LinealInterpolation.interpolate(x1=index - 1,
                                                           x2=lightIntensity[index - 1],
                                                           y1=index + 1,
                                                           y2=lightIntensity[index + 1],
                                                           x=index)
                if np.isinf(newValue) or np.isnan(newValue):
                    newValue = lightIntensity[index - 1]
                lightIntensity[index] = int(newValue)
        lightExport.append(value)

    for index, value in temperature.items():
        if value < tempLowerLimit or value > tempUpperLimit:
            print(f'Temperature Outlier: {value}')
            if index == 0:
                temperature[index] = temperature[index + 1]
            elif index == len(temperature) - 1:
                temperature[index] = temperature[index - 1]
            else:
                newValue = LinealInterpolation.interpolate(x1=index - 1,
                                                           x2=temperature[index - 1],
                                                           y1=index + 1,
                                                           y2=temperature[index + 1],
                                                           x=index)
                if np.isinf(newValue) or np.isnan(newValue):
                    newValue = temperature[index - 1]
                temperature[index] = int(newValue)
                print(f'New Temperature Value: {int(newValue)}')
        temperatureExport.append(value)

    x = [i for i in range(len(lightIntensity))]

    if plotCheck == 0:
        plt.plot(x, lightIntensity, label='Luz REAL', color='blue')
        lightIntensity_smooth = SES.calc_suavizado_exponencial(lightIntensity, 0.9)
        plt.plot(x, lightIntensity_smooth, label='Luz Smooth', color='green')
        plt.title('Light Intensity')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)
    else:
        plt.plot(x, temperature, label='Temperatura Real', color='red')
        temperature_smooth = SES.calc_suavizado_exponencial(temperature, 0.9)  # Fixed this line
        plt.plot(x, temperature_smooth, label='Temperatura Smooth', color='yellow')
        plt.title('Temperature')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.legend()
        plt.grid(True)

    plt.show()

    with open(f'sensor_readings{readingNumber}_treated.csv', mode='w') as file:
        for i in range(len(lightExport)):
            line = f'{lightExport[i]},{temperatureExport[i]}\n'
            file.write(line)

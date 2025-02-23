import numpy as np
import matplotlib.pyplot as plt
from Practicas.Utils import MetricasDeError as mde


def calcularSuavizadoExponencial(serie, alfa):
    # alfa controla el peso que se le da a los datos
    # valores cercanos a 1 hacen que los datos recientes tiene mas influencia
    # valores cercanos a 0 dan mas importancia a los datos antiguos
    newSerie = np.zeros_like(serie)
    newSerie[0] = serie[0]
    for t in range(1, len(serie)):
        newSerie[t] = alfa * serie[t] + (1 - alfa) * newSerie[t - 1]
    return newSerie


readingNumber = ''
dataset = np.loadtxt(fname=f'sensor_readings{readingNumber}_treated.csv', delimiter=',')
datos = dataset[:, 0]
alfas = [round(i * 0.1, 1) for i in range(1, 10)]

for alfa in alfas:
    serieSuavizada = calcularSuavizadoExponencial(datos, alfa)

    errorMAE = mde.calcularMAE(datos, serieSuavizada)
    errorMSR = mde.calcularMSE(datos, serieSuavizada)
    errorRMSE = mde.calcularRMSE(datos, serieSuavizada)
    errorMAPE = mde.calcularMAPE(datos, serieSuavizada)

    print("Alfa: ", alfa)
    print("MAE: ", errorMAE)
    print("MSR: ", errorMSR)
    print("RMSE: ", errorRMSE)
    print("MAPE: ", errorMAPE, "\n")

    x = [i for i in range(1, len(serieSuavizada) + 1)]
    plt.figure(figsize=(12, 6))
    plt.plot(x, datos, label="REAL", color="blue")
    plt.plot(x, serieSuavizada, label="SMOOTH", color="green")
    plt.title("Comparacion de Series")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
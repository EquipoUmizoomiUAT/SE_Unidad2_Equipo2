import numpy as np


def calcularMAE(valoresReales, valoresEstimados):   # Error Absoluto Medio
    # Sumatoria de la diferencias absolutas de los valores, entre el numero de elementos
    # Mide el error medio en las mismas unidades que los datos reales. Mas bajo es mejor
    MAE = np.mean(np.abs(valoresReales - valoresEstimados))
    return MAE


def calcularMSE(valoresReales, valoresEstimados):    # Error Cuadratico Medio (MSE)
    # Sumatoria del cuadrado de las diferencias, entre el numero de elementos
    MSE = np.mean((valoresReales - valoresEstimados) ** 2)
    return MSE


def calcularRMSE(valoresReales, valoresEstimados):  # Raiz del Error Cuadratico Medio
    # Raiz cuadrada del MSE
    # Penaliza mas a los errores grandes, Pone al aerroe en las mismas unidades que los datos reales
    MSE = calcularMSE(valoresReales, valoresEstimados)
    RMSE = np.sqrt(MSE)
    return RMSE


def calcularMAPE(valoresReales, valoresEstimados):  # Error Porcentual Absoluto Medio
    # Mide el error en porcentaje. Facilita la interpretacino en terminos relativos
    MAPE = np.mean(np.abs((valoresReales - valoresEstimados) / valoresReales)) * 100
    return MAPE
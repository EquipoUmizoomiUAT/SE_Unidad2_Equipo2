import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings

warnings.simplefilter('ignore')

if __name__ == '__main__':
    # Semana 1 Luz : d = 1, Temp : d = 1
    # Semana 2 Luz : d = 1, Temp : d = 1
    # Semana 3 Luz : d = 1 Temp : d = 1
    readingNumber = '2'
    dataset = np.loadtxt(fname=f'sensor_readings{readingNumber}_treated.csv', delimiter=',')
    # 0 Luz
    # 1 Temperatura
    datos = dataset[:, 1]

    d = 1
    p_values = [1, 2, 3, 4, 5, 6, 7, 8, 10]
    q_values = [1]

    best_aic = 999999
    best_model = None
    best_order = None

    for p in p_values:
        for q in q_values:
            try:
                model = ARIMA(datos, order=(p, d, q)).fit()
                aic = model.aic
                print(f'Parametros -> p: {p}, q: {q}, AIC: {aic:.2f}')

                if aic < best_aic:
                    best_aic = aic
                    best_model = model
                    best_order = (p, d, q)
            except:
                print(f'Parametros -> p: {p}, q: {q}, COMBINACION NO VALIDA')

    print(f'Mejor modelo: ARIMA({best_order}) con AIC = {best_aic:.2f}')

    plt.figure(figsize=(10, 5))
    plt.plot(datos, label='Data', color='blue')
    plt.plot(best_model.fittedvalues, label='Mejor ARIMA', linestyle='--', color='red')
    plt.show()
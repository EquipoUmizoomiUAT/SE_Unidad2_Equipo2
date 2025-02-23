import numpy as np
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

if __name__ == '__main__':
    '''
        Semana 1:
            Luz:
                d = 1
                q = 1
                p = 1, 2, 3, 4
            Temperatura:
                d = 1
                q = 1
                p = 1, 2, 3, 4, 5, 6, 7, 8, 9
        Semana 2:
            Luz:
                d = 1
                q = 1, 2, 8
                p = 1, 2, 3, 5, 7
            Temperatura:
                d = 1
                q = 1
                p = 1, 2, 3, 4, 5, 6, 7, 8, 10
        Semana 3:
        (checar)
            Luz:
                d = 1
                q = 1, 2, 7, 8
                p = 1, 2, 3, 4, 5, 7, 8, 10
            Temperatura:
                d = 1
                q = 1
                p = 1, 2, 3, 4, 5, 6, 7, 10
    '''
    readingNumber = ''
    dataset = np.loadtxt(fname=f'sensor_readings{readingNumber}_treated.csv', delimiter=',')
    datos = dataset[:, 0]
    datos = np.diff(datos)
    datos = np.diff(datos)



    plt.figure(figsize=(12, 5))

    # Creacion de ejes
    ax1 = plt.subplot(121)
    ax2 = plt.subplot(122)

    # De acuerdo con la libreria, se tiene que tomar en cuenta el tamano de la serie, en ese sentido, para este ejemplo
    # se tiene el maximo de lags es 6:
    # ValueError: Can only compute partial correlations for lags up to 50% of the sample size. The requested nlags 10 must be < 6.

    # Grafica ACF (identifica q)
    plot_acf(datos, lags=10, ax=ax1)  # lags=10)

    # Grafica PACF (identifica p)
    plot_pacf(datos, lags=10, ax=ax2)  # lags=10)

    plt.show()
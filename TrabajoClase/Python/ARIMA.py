from statsmodels.tsa.arima.model import ARIMA
import numpy as np

readingNumber = ''
dataset = np.loadtxt(fname=f'sensor_readings{readingNumber}_treated.csv', delimiter=',')
# 0 Luz
# 1 Temperatura
datos = dataset[:, 0]

p = 1
d = 1
q = 2
modelo = ARIMA(datos, order=(p, d, q))  # ARIMA(p,d,q)
ajuste = modelo.fit()
pronostico = ajuste.forecast(steps=1)

print("Pronóstico:", pronostico[0])

#S la series es NO ESTAACIONARIA, aparecera esta advertencia:
# UserWarning: Non-stationary starting autoregressive parameters found
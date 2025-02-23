from statsmodels.tsa.arima.model import ARIMA


def calculateARIMA(series):
    p = 1
    q = 1
    d = 3
    model = ARIMA(series, order=(p, q, d))
    ajuste = model.fit()
    return ajuste.forecast(steps=len(series))

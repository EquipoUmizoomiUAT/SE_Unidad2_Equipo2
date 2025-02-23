import numpy as np
import json
import pandas as pd


if __name__ == '__main__':
    data = np.zeros((6, 6, 100))    # No. Pin x Medida Estadistica x No. Lectura
    with open(file='u2p3exportRaw.txt', mode='r') as f:
        for i in range(99):
            print(f'Leyendo lectura {i}')
            line = f.readline().strip()
            sensorData = json.loads(line)
            for pin in range(6):
                data[pin, 0, i] = sensorData[f"Pin {pin}"]["Last Value"]
                data[pin, 1, i] = sensorData[f"Pin {pin}"]["Average"]
                data[pin, 2, i] = sensorData[f"Pin {pin}"]["Median"]
                data[pin, 3, i] = sensorData[f"Pin {pin}"]["Max"]
                data[pin, 4, i] = sensorData[f"Pin {pin}"]["Min"]
                data[pin, 5, i] = sensorData[f"Pin {pin}"]["Mode"]

    sd = np.zeros((6, 6))
    for pin in range(6):
        for measureMode in range(6):
            print(f'Pin {pin} : Medida {measureMode}')
            sd[pin, measureMode] = np.std(data[pin, measureMode])

    df = pd.DataFrame(sd, columns=['Ultimo Valor', 'Media', 'Mediana', 'V. Maximo', 'V. Minimo', 'Moda'])
    print(df)

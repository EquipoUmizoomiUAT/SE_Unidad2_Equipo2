from serial.serialutil import SerialException
from Practicas.Utils import SES, ARIMA
import serial
import time as t


def WriteArduino(value):
    if value < 50:
        arduino.write('0'.encode('utf-8'))
        return
    if value < 100:
        arduino.write('1'.encode('utf-8'))
        return
    if value < 150:
        arduino.write('2'.encode('utf-8'))
        return
    arduino.write('3'.encode('utf-8'))


if __name__ == "__main__":
    day = 1
    days = {
        1: 'Lunes',
        2: 'Martes',
        3: 'Miercoles',
        4: 'Jueves',
        5: 'Viernes',
        6: 'Sabado',
        7: 'Domingo'
    }
    time = 0
    serie = []
    arduino = serial.Serial(port='com3', baudrate=9600, timeout=10)
    while True:
        try:
            value = arduino.readline()
            if day == 1:
                if time < 23:
                    print('Se leyo valor de arduino')
                    value = int(value.decode('utf-8').strip())
                    serie.append(value)
                    WriteArduino(value)
                    time += 1
                else:
                    day += 1
                    time = 0
            else:
                if day < 8:
                    if time == 0:
                        print(f'Predijiendo valores para el dia {days[day]}')
                        #serie = SES.calc_suavizado_exponencial(serie, 0.5)
                        serie = ARIMA.calculateARIMA(serie)
                    if time < 23:
                        WriteArduino(serie[time])
                        time += 1
                    else:
                        time = 0
                        day += 1
                else:
                    day = 1
                    time = 0
                    serie = []
            print(f'Es {days[day]} a las {time}:00 horas, la luz es de {value if day == 1 else serie[time]}')
            t.sleep(3)
        except SerialException:
            print("Something went berry wrong with Arduino")
        except UnicodeDecodeError:
            print("Something went berry wrong with Decoding")
        except KeyboardInterrupt:
            print("I noticed something berry wrong")
        except Exception as e:
            print(f'The wrongest of berries {e}')

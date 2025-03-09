from serial.serialutil import SerialException
from Practicas.Utils import PromedioPonderado as PP, ARIMA
from Practicas.Utils import SES
import serial
import time as t
# inter pol y ouliers

def WriteArduino(value):
    if value < 256:
        arduino.write('0'.encode('utf-8'))
        return
    if value < 512:
        arduino.write('1'.encode('utf-8'))
        return
    if value < 768:
        arduino.write('2'.encode('utf-8'))
        return
    arduino.write('3'.encode('utf-8'))


if __name__ == "__main__":
    w = 0.8
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
            value = int(arduino.readline().decode('utf-8').strip())
            if day == 1:
                if time < 24:
                    print('Se leyo valor de arduino')
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
                        serie = ARIMA.calculateARIMA(serie)
                    if time < 24:
                        value = PP.PromedioPonderado(value, serie[time], w)
                        WriteArduino(value)
                        time += 1
                    else:
                        time = 0
                        day += 1
                else:
                    day = 1
                    time = 0
                    serie = []
            print(f'Es {days[day]} a las {time - 1}:00 horas, la luz es de {value if day == 1 else serie[time]}')
            t.sleep(3)
        except SerialException:
            print("Something went berry wrong with Arduino")
        except UnicodeDecodeError:
            print("Something went berry wrong with Decoding")
        except KeyboardInterrupt:
            print("I noticed something berry wrong")
        except Exception as e:
            print(f'The wrongest of berries {e}')

import serial

if __name__ == "__main__":
    arduino = serial.Serial(port='com3', baudrate=9600, timeout=1)
    readings = 0
    with open(file='u2p3exportRaw.txt', mode='w') as file:
        while readings <= 100:
            try:
                line = arduino.readline().decode().strip()
                print(f'{readings} {line}')
                file.write(line + '\n')
                readings += 1
            except serial.SerialException:
                print('Arduino Error')
            except UnicodeDecodeError:
                print("Bad parse")
            except Exception as e:
                print(e)

import serial


def ReadValuesMonday():
    arduino = serial.Serial(port='com3', baudrate=9600, timeout=1)
    export = []
    while len(export) <= 24:
        try:
            if arduino.in_waiting > 0:
                print("Leyendo valor " + str(len(export)))
                reading = arduino.readline().decode().strip()
                export.append(reading)
        except:
            print("Bad Reading")

    with open(file="exportU2P5.csv", mode="w", encoding="utf-8") as exportFile:
        for reading in export:
            exportFile.write(reading + "\n")

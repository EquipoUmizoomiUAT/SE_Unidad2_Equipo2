import serial

if __name__ == "__main__":
    arduino = serial.Serial('com3', baudrate=9600, timeout=1)
    export = []
    while len(export) < 100:
        try:
            reading = arduino.readline().decode().strip().split(",")
            export.append(reading)
        except:
            print("Bad Reading")

    with open(file="u2p1export.csv", mode="w", encoding="utf-8") as exportFile:
        for reading in export:
            exportFile.write(",".join(reading) + "\n")

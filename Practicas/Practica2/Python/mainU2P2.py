import serial
import csv
from datetime import datetime
import time
import requests

# Configure the serial port
arduino = serial.Serial('COM3', 9600)  # Replace 'COM3' with your Arduino's serial port
print('Aridono connecto')
# Telegram bot details
bot_token = '8048512753:AAFUfd_3KzdTBJ1z9UMgNSheaK6OOqdVsUY'
chat_id = '7579784242'
readingnumber = 4


def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {'chat_id': chat_id, 'text': message}
    try:
        response = requests.post(url, data=data)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error sending message: {e}")


# Open the CSV file for writing
with open(f'sensor_readings{readingnumber}.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['ReadingIndex', 'LightIntensity', 'Temperature', 'Date', 'Time'])
    print('process start')
    index = 1
    start_time = time.time()
    while True:
        # Check if there is data in the serial buffer
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            if line:
                try:
                    light_intensity, temperature = line.split(',')
                    now = datetime.now()
                    date = now.strftime('%Y-%m-%d')
                    time_str = now.strftime('%H:%M:%S')

                    # Write the data to the CSV file
                    writer.writerow([index, light_intensity, temperature, date, time_str])
                    print(f"Reading {index}: LightIntensity={light_intensity}, Temperature={temperature}, Date={date}, Time={time_str}")

                    # Send the reading to the Telegram bot
                    message = f"Reading {index}: LightIntensity={light_intensity}, Temperature={temperature}, Date={date}, Time={time_str}"
                    send_telegram_message(message)

                    index += 1
                except ValueError:
                    print("Error parsing data")
                except Exception as e:
                    print(f"Unexpected error: {e}")

        # Check if 24 hours have passed
        if time.time() - start_time >= 24 * 3600:
            break

        # Small delay to prevent high CPU usage
        time.sleep(1)
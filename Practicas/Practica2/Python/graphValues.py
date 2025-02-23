import pandas as pd
import matplotlib.pyplot as plt


def graphValuesTime(csv_file):
    # Get the data
    df = pd.read_csv(csv_file)

    # Combine Date and Time to DateTime
    df['DateTime'] = pd.to_datetime(df['Date'] + ' ' + df['Time'])

    plt.figure(figsize=(12, 6))

    plt.plot(df['DateTime'], df['Temperature'], label='Temperature', color='r')
    plt.plot(df['DateTime'], df['LightIntensity'], label='Light Intensity', color='b')

    plt.xlabel('Time')
    plt.ylabel('Values')
    plt.title('Temperatura e Intensidad Luminosa')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Show the plot
    plt.show()


if __name__ == '__main__':
    graphValuesTime('sensor_readings.csv')
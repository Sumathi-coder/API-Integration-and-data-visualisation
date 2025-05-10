import requests
import matplotlib.pyplot as plt
from datetime import datetime

# Replace with your actual OpenWeatherMap API key
API_KEY = 'your_api_key_here'
CITY = 'London'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data: {response.status_code}")
        return None

def parse_weather_data(data):
    timestamps = []
    temperatures = []

    for entry in data['list']:
        # Convert timestamp
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']

        timestamps.append(dt)
        temperatures.append(temp)

    return timestamps, temperatures

def plot_temperature(timestamps, temperatures):
    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, temperatures, marker='o', linestyle='-', color='b')
    plt.title(f"5-Day Temperature Forecast for {CITY}")
    plt.xlabel("Date and Time")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def main():
    data = fetch_weather_data()
    if data:
        timestamps, temperatures = parse_weather_data(data)
        plot_temperature(timestamps, temperatures)

if __name__ == "__main__":
    main()
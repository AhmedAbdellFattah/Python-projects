import tkinter as tk
from tkinter import ttk
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather App")

        self.location_label = ttk.Label(root, text="Location:")
        self.location_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

        self.location_entry = ttk.Entry(root, width=30)
        self.location_entry.grid(row=0, column=1, padx=5, pady=5)

        self.search_button = ttk.Button(root, text="Search", command=self.get_weather)
        self.search_button.grid(row=0, column=2, padx=5, pady=5)

        self.temperature_label = ttk.Label(root, text="Temperature:")
        self.temperature_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.humidity_label = ttk.Label(root, text="Humidity:")
        self.humidity_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")

        self.wind_speed_label = ttk.Label(root, text="Wind Speed:")
        self.wind_speed_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")

        self.pressure_label = ttk.Label(root, text="Pressure:")
        self.pressure_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")

        self.precipitation_label = ttk.Label(root, text="Precipitation:")
        self.precipitation_label.grid(row=5, column=0, padx=5, pady=5, sticky="w")

    def get_weather(self):
        location = self.location_entry.get()
        api_key = "f0d2b39320cf9c7bd2852827a998d747"
        base_url = "http://api.openweathermap.org/data/2.5/weather"
        params = {"q": location, "appid": api_key, "units": "metric"}

        try:
            response = requests.get(base_url, params=params)
            response.raise_for_status()
            data = response.json()

            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            pressure = data["main"]["pressure"]
            precipitation = data["clouds"]["all"]

            self.temperature_label.config(text=f"Temperature: {temperature}°C")
            self.humidity_label.config(text=f"Humidity: {humidity}%")
            self.wind_speed_label.config(text=f"Wind Speed: {wind_speed} km/h")
            self.pressure_label.config(text=f"Pressure: {pressure} hPa")
            self.precipitation_label.config(text=f"Precipitation: {precipitation}%")

            # Update the UI
            self.temperature_label.update()
            self.humidity_label.update()
            self.wind_speed_label.update()
            self.pressure_label.update()
            self.precipitation_label.update()

        except requests.exceptions.RequestException as e:
            print(f"Error during weather request: {e}")
            # You might want to display an error message to the user here

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

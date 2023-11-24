import tkinter as tk
from tkinter import messagebox
import requests

class WeatherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Weather Forecast App")
        self.root.geometry("400x300")
        self.api_key = "e10c391fc9ef1b0181009e9bfce855cc"

        self.title_label = tk.Label(root, text="Weather Forecast", font=("Helvetica", 16, "bold"))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(10, 20))

        self.location_label = tk.Label(root, text="Location:")
        self.location_label.grid(row=1, column=0, sticky="e", padx=10)

        self.location_entry = tk.Entry(root)
        self.location_entry.grid(row=1, column=1, pady=10)

        self.search_button = tk.Button(root, text="Search", command=self.get_weather)
        self.search_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.temperature_label = tk.Label(root, text="Temperature: ")
        self.temperature_label.grid(row=3, column=0, columnspan=2, pady=5)

        self.humidity_label = tk.Label(root, text="Humidity: ")
        self.humidity_label.grid(row=4, column=0, columnspan=2, pady=5)

        self.wind_speed_label = tk.Label(root, text="Wind Speed: ")
        self.wind_speed_label.grid(row=5, column=0, columnspan=2, pady=5)

        self.pressure_label = tk.Label(root, text="Pressure: ")
        self.pressure_label.grid(row=6, column=0, columnspan=2, pady=5)

        self.precipitation_label = tk.Label(root, text="Precipitation: ")
        self.precipitation_label.grid(row=7, column=0, columnspan=2, pady=5)

    def get_weather(self):
        location = self.location_entry.get()
        if not location:
            messagebox.showinfo("Info", "Please enter a location.")
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={self.api_key}&units=metric"
            response = requests.get(url)
            data = response.json()

            temperature = f"Temperature: {data['main']['temp']}°C"
            humidity = f"Humidity: {data['main']['humidity']}%"
            wind_speed = f"Wind Speed: {data['wind']['speed']} km/h"
            pressure = f"Pressure: {data['main']['pressure']} hPa"
            precipitation = f"Precipitation: {data.get('rain', {'1h': 0}).get('1h', 0)}%"

            self.temperature_label.config(text=temperature)
            self.humidity_label.config(text=humidity)
            self.wind_speed_label.config(text=wind_speed)
            self.pressure_label.config(text=pressure)
            self.precipitation_label.config(text=precipitation)

        except Exception as e:
            messagebox.showinfo("Info", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WeatherApp(root)
    root.mainloop()

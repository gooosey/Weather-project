# Imports
import requests
import customtkinter
from datetime import datetime

# Load the API key
with open('api_key.txt', 'r') as file:
    APIKey = file.read().strip()  # https://openweathermap.org/api

# Main app class
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # App settings
        self.title("Wether")
        self.geometry("300x300")
        self.resizable(width=False, height=False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        # Label
        self.label = customtkinter.CTkLabel(self, text="Submit a Place", font=("Arial", 30), fg_color="transparent")
        self.label.pack(side="top", padx=20, pady=30)

        # Textbox for user input
        self.textbox = customtkinter.CTkTextbox(master=self, width=200, height=20, corner_radius=10, font=("Arial", 20))
        self.textbox.pack(side="top", padx=20, pady=25)

        # Button to gather info
        self.button1 = customtkinter.CTkButton(self, text="open", command=self.inphandle)
        self.button1.pack(side="top", padx=20, pady=20)

        self.tlwindow = None

    # Grabs data
    def inphandle(self):
        city = self.textbox.get("1.0", "end").strip()

        # Checks if city is entered
        if not city:
            print("Error: No city entered")
            return

        # Initiate URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}&units=metric"

        # Grabbing data
        try:
            # Request data
            Response = requests.get(url)
            WeatherData = Response.json()

            # Extract necessary data
            LocationName = WeatherData['name']
            LocationTemp = WeatherData['main']['temp']
            CaptureTime = WeatherData['dt']  # Unix timestamp
            CaptureTimeFormatted = datetime.utcfromtimestamp(CaptureTime).strftime('%Y-%m-%d %H:%M:%S UTC')

            print(f"Weather for {LocationName}")
            print(f"Temp is {LocationTemp}C")
            print(f"Data captured at {CaptureTimeFormatted}")

            self.opentop(LocationName, LocationTemp, CaptureTimeFormatted)

        except requests.exceptions.RequestException as e:
            self.errors("Please check your internet")

        except KeyError:
            self.errors("Place not found")

    def errors(self, message):
        ewindow = customtkinter.CTkToplevel(self)
        ewindow.geometry("300x50")
        elabel = customtkinter.CTkLabel(ewindow, text=message, font=("Arial", 30))
        elabel.pack(pady=10)

    # Checks if window exists or creates a new window
    def opentop(self, LocationName, LocationTemp, CaptureTimeFormatted):
        if self.tlwindow is None or not self.tlwindow.winfo_exists():
            # Creates new window
            self.tlwindow = toplevelwindow(self, LocationName, LocationTemp, CaptureTimeFormatted)
        else:
            self.tlwindow.focus()


# Second display
class toplevelwindow(customtkinter.CTkToplevel):
    def __init__(self, master, city_name, city_temp, capture_time):
        super().__init__(master)
        self.geometry("400x200")
        self.title("Weather Info")

        self.label_city = customtkinter.CTkLabel(self, text=f"Location: {city_name}", font=("Arial", 18))
        self.label_city.pack(pady=10)

        self.label_temp = customtkinter.CTkLabel(self, text=f"Temperature: {city_temp}°C", font=("Arial", 18))
        self.label_temp.pack(pady=10)

        self.label_time = customtkinter.CTkLabel(self, text=f"They took me at:\n {capture_time}", font=("Arial", 18))
        self.label_time.pack(pady=10)


# Start the app
app = App()
app.mainloop()

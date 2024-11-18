# Imports
import requests
import json
from typing import Tuple
import customtkinter
import tkinter

# Dont look at my API please
with open('api_key.txt', 'r') as file:
    APIKey = file.read().strip() 

# Secound display
class toplevelwindow(customtkinter.CTkToplevel):
    def __init__(self, *args,**kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("400x300")

        self.label = customtkinter.CTkLabel(self, text="Testing")
        self.label.pack(padx=20, pady=20)

# Current display
class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        #App miscellaneous 
        self.title("Wether")
        self.geometry("300x300")
        self.resizable(width=False,height=False)
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        
        # Label
        self.label = customtkinter.CTkLabel(self, text="Submit a country", font= ("Arial", 25), fg_color="transparent")
        self.label.pack(side="top", padx= 20, pady= 20)

        # Textbox for users input
        self.textbox = customtkinter.CTkTextbox(master=self, width= 200, height= 100, corner_radius=0)
        self.textbox.pack(side="top", padx= 20, pady= 20)


        # Button to open new window
        self.button1 = customtkinter.CTkButton(self,text="open", command=self.inphandle)
        self.button1.pack(side="top", padx= 20, pady= 20)
        
        self.tlwindow = None


    # Takes input and opens func opentop
    def inphandle(self):
        city = self.textbox.get("1.0", "end").strip()
        # Initate url
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={APIKey}&units=metric"

        # Grabbing data
        try:
            # Asking for data 
            Response = requests.get(url)
            WeatherData = Response.json()

            Cityname = WeatherData['name']
            Citytemp = WeatherData['main']['temp']

            print(f'Weather for {Cityname}')
            print(f'Temp is {Citytemp}C')

        except requests.exceptions.RequestException as e:
            print("Check your internet")
            print(e)

        except KeyError:
            print("try again")
        
        self.opentop()


    # Checks if window exists or creates windows
    def opentop(self):
        if self.tlwindow is None or not self.tlwindow.winfo_exists():
            # Creates new window
            self.tlwindow = toplevelwindow(self) 
        else:
            self.tlwindow.focus()

# Start the app up
app = App()
app.mainloop()


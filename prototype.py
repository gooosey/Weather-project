import tkinter as tk
import requests

def get_user_location():
    # Use a geolocation API to get the user's location based on IP
    response = requests.get('https://ipinfo.io')
    location_data = response.json()

    # Extract the city from the data
    city = location_data.get('city', 'City not found')
    result_label.config(text=f"You are in {city}")

# Set up the Tkinter window
root = tk.Tk()
root.title("Location Finder")

# Create widgets
ask_label = tk.Label(root, text="Would you like to know your city?")
ask_label.pack(pady=5)

yes_button = tk.Button(root, text="Yes", command=get_user_location)
yes_button.pack(pady=10)

no_button = tk.Button(root, text="No", command=lambda: result_label.config(text="Okay, no city information."))
no_button.pack(pady=10)

result_label = tk.Label(root, text="City info will appear here")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()

# ============================================
# STEP 1: IMPORT LIBRARIES
# ============================================ 
import os
import requests
import matplotlib.pyplot as plt 

# ============================================
# STEP 2: CONFIGURATION
# ============================================
# TODO: Replace with your actual API key from OpenWeatherMap
API_KEY = os.getenv("OPENWEATHER_API_KEY")

# Base URL for the weather API
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# Cities we want to compare
cities = ["London", "Tokyo", "New York", "Sydney", "Dubai"]

# ============================================
# STEP 3: FUNCTION TO GET TEMPERATURE
# ============================================
def get_temperature(city_name):
    
    # Create parameters for the API request
    params = {
        'q': city_name,           # City name
        'appid': API_KEY,         # Your API key
        'units': 'metric'         # Get temperature in Celsius
    }
    
    # try and except is used because something could go wrong when requesting the weather data.
    #And we don't want the whole program to crash.
    try:
        response = requests.get(BASE_URL,params=params)
        
        # TODO: Convert the response to JSON (a Python dictionary)
        data = response.json()
        
        # TODO: Extract the temperature from the data
        #hint: extract both data points using variable['main']['temp']
        temperature = data["main"]["temp"]
        
        return temperature
    
    except Exception as e:
        #print statements, be sure to f print including {city_name}: {e}
        print(f"Error getting weather for {city_name}: {e}")
        return None


# ============================================
# STEP 4: COLLECT DATA FOR ALL CITIES
# ============================================
# TODO: Create two empty lists
# One for city names, one for temperatures
city_names = []
temperatures = []

print("Fetching weather data...\n")

# TODO: Loop through each city in the cities list
# For each city:
#   1. Call get_temperature(city)
#   2. If temp is not None, add city and temp to your lists
#   3. Print a success message

# Your loop here:
for city in cities:
    # Your code here
    temp = get_temperature(city)

    if temp is not None:
        city_names.append(city)
        temperatures.append(temp)
        print(f"Got weather for {city}: {temp}°C")

# ============================================
# STEP 5: CREATE THE VISUALIZATION
# ============================================
# Create a figure with size 10x6
# Feel free to change plt to a different variable name if you want, but remember it is the variable responsible for your graph!
plt.figure(figsize=(10, 6))


# TODO: Create a bar chart
# Hint: .bar(var1, var2, color = 'exampleColor')
plt.bar(city_names, temperatures, color = "Blue")

# TODO: Add labels for x-axis: .xlabel() and y-axis: .ylabel() 
# Use this °C for Celsius
plt.xlabel("Cities")
plt.ylabel("Temperature (°C)")

# TODO: Add a .title() to the chart
plt.title("Current Temperatures Around the World")

# TODO: Add temperature values on top of each bar
# Hint: Use a for loop with enumerate(temperatures)
for i, temp in enumerate(temperatures):
    plt.text(i, temp, f"{temp}°C", ha="center")

# TODO: Make the chart look nice with a .grid()
plt.grid()

# TODO: Use .tight_layout() to prevent labels from being cut off
plt.tight_layout()

# TODO: Display the chart
#Hint: use .show()
plt.savefig("weather_chart.png")
plt.show()
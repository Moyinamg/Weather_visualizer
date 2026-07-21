# Weather Data Visualizer 🌤️

A Python-based weather data visualization project that retrieves real-time temperature data for cities around the world and presents the results in a clear bar chart.

## Overview

The Weather Data Visualizer uses live weather data to compare current temperatures across multiple cities. The program retrieves data from the OpenWeather API, processes the JSON response, extracts the temperature for each city, and uses Matplotlib to create a visual comparison.

The project currently compares weather data for:

- London
- Tokyo
- New York
- Sydney
- Dubai

## Features

- Retrieves current temperature data from a weather API
- Processes JSON data returned by the API
- Collects and organizes weather data for multiple cities
- Handles errors when weather data cannot be retrieved
- Displays temperatures in Celsius
- Creates a bar chart to compare temperatures across cities
- Displays temperature values directly on the chart
- Uses environment variables to keep sensitive information out of the source code

## Technologies Used

- **Python** – Main programming language used to build the project
- **Requests** – Sends requests to the weather API and retrieves data
- **Matplotlib** – Creates the weather data visualization
- **OpenWeather API** – Provides current weather data
- **JSON** – Format used to receive and process weather data

## How It Works

1. The program starts with a list of cities to compare.
2. It sends a request to the OpenWeather API for each city.
3. The API returns current weather information in JSON format.
4. The program extracts the temperature from the returned data.
5. Successful results are stored and organized into lists.
6. Matplotlib uses the collected data to create a bar chart comparing the temperatures.
7. Each bar is labeled with its corresponding temperature for easier comparison.

## What I Learned

Through this project, I gained more hands-on experience working with APIs and real-world data in Python. I practiced retrieving and processing JSON data, creating and calling functions, working with lists and loops, and handling possible errors.

I also learned how to use Matplotlib to turn collected data into a visual representation and how environment variables can be used to keep sensitive information separate from public source code.

## Future Improvements

Possible future improvements include:

- Allowing users to enter their own cities
- Displaying additional weather information such as humidity and weather conditions
- Adding more visualization options
- Comparing weather data over multiple days

## Project Status

This project was created as part of my Python learning experience and demonstrates my understanding of working with APIs, JSON data, data visualization, and Python fundamentals.

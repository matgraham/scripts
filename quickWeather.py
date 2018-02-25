#! python3
# quickWeather.py - Prints the weather for a location from the command line

import json, requests, sys

# Compute location for command line arguments
if len(sys.argv) < 2:
    print('Usage: quickWeather.py location')
    sys.exit()
location = ''.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = 'http://api.openweathermap.org/data/2.5/forecast?id=%s&APPID=800e268a6bf87a5cf0bd83716b5c05b1' % (location)
response = requests.get(url)
response.raise_for_status()

# Load JSON data into a python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('Current weather in %s:' % (location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
print()
print('Tomorrow:')
print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
print()
print('Day after tomorrow:')
print([w][2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])

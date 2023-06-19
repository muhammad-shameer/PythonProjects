import requests
import json
import os

city = input("Enter the name of a city: ")
url = f"https://api.weatherapi.com/v1/current.json?key=1a0597ce19a74df481b101323231906&q={city}"

request = requests.get(url)
# print(request.text)
weather_dict = json.loads(request.text)  # convert string to dictionary

weather_c = weather_dict["current"]["temp_c"]  # temperature in celsius

print(f"The current weather in { city } is { weather_c }")
os.system(f"say 'The current weather in { city } is { weather_c }'")

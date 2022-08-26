import json
import requests
import time
import webbrowser
from pprint import pprint
from win10toast_click import ToastNotifier

toast = ToastNotifier()

# get all data
api_key = "xxxx"
#city_name = input('Enter your city : ')
#units_input = input ('Which measurement system do you use? (i - imperial, m - metric) : ')
get_weather = r"http://api.openweathermap.org/data/2.5/weather?q=Mrkonjic%20Grad" #+ city_name
units = "metric"

# if units_input == "i":
#    units = "imperial"
#elif units_input == "m":
#    units = "metric"
#else:
#    print("wrong input, default metric units applies...")
#    units = "metric"
#

# check which units are used
if units == "metric":
    temp_symbol = "C"
else:
    temp_symbol = "F"

toast.show_toast("Thank you!", duration=5, msg="This proccess will now run in the background.\nNo need to start it up again.")

weather_site = "https://openweathermap.org/city/"

def open_site():
    try:
        webbrowser.open(weather_site + str(city_id))
    except:
        toast.show_toast("Something went wrong...", duration=5, msg="Failed to reach OpenWeatherMap\nPlease check your connection. This may be an error with the server, so try again later.")


time.sleep(3)

# loop
while True:
    # get data from API
    r = requests.get(get_weather + "&appid=" + api_key + "&units=" + units)
    data = r.json()

    temperature = data['main']['temp']
    wind_speed = data['wind']['speed']
    weather_desc = data['weather'][0]['description']
    city_id = data['id']

    # print formatted data to console
    pprint(data)

    # show notification
    toast.show_toast("Weather Update (click for info)", duration=30, msg="Current temperature is " + str(temperature) + "°" + temp_symbol + '.\nWind speed is {}m/s'.format(wind_speed) + '\nWeather is {}'.format(weather_desc), callback_on_click=open_site)

    time.sleep(10800)



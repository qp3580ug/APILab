import requests
import os

def main():
    key = os.environ.get('WEATHER_KEY')
    city = input('What city would you like the weather for? ')
    country = input('What country is this city in?(Please use the 2 letter country code) ')
    cityCountry = city + ',' + country
    query = {'q': cityCountry, 'units': 'imperial', 'appid': key}

    url = 'http://api.openweathermap.org/data/2.5/forecast'
    data = requests.get(url, params=query).json()
    date = 0

    print('The Following is your 5 day forecast every 3 hours.')

    while date < 40:
        weather_temp = data['list'][date]['main']['temp']
        weather_description = data['list'][date]['weather'][0]['description']
        wind_speed = data['list'][date]['wind']['speed']
        date_time = data['list'][date]['dt_txt']
        '''I decided to go with UTC so that they can see the local Date and Time for where they are searching'''

        print(f'Date & Time: {date_time}\nTemperature: {weather_temp:.2f}F\nWeather Description: {weather_description}\nWind Speed: {wind_speed:.2f}MPH\n')  

        date += 1

    else:
        print('This was your 5 day forecast!!')

if __name__ == '__main__':
    main()
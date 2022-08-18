import datetime as dt
import requests
import re

API_KEY = 'go to https://api.openweathermap.org and create an account and get an API KEY'


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def get_weather(lat, lon):
    base_url = 'https://api.openweathermap.org/data/2.5/weather?'
    url = base_url + 'lat=' + str(lat) + '&lon=' + str(lon) + '&appid=' + API_KEY
    response = requests.get(url).json()
    return response


def get_lat_lon(city):
    base_url = 'http://api.openweathermap.org/geo/1.0/direct'
    url = base_url + '?q=' + city + '&limit=1&appid=' + API_KEY
    response = requests.get(url).json()
    return response[0]['lat'], response[0]['lon']


def print_weather_data(response, city):
    weather_description = response['weather'][0]['description']

    kelvin_temp = response['main']['temp']
    celsius_tmp = kelvin_to_celsius(kelvin_temp)

    kelvin_temp_max = response['main']['temp_max']
    celsius_tmp_max = kelvin_to_celsius(kelvin_temp_max)

    kelvin_temp_min = response['main']['temp_min']
    celsius_tmp_min = kelvin_to_celsius(kelvin_temp_min)

    sunrise = str(dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone']))
    sunrise = re.findall('[\w\-]+\s(.*)', sunrise)
    sunset = str(dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone']))
    sunset = re.findall('[\w\-]+\s(.*)', sunset)

    print(f'temperature in {city}: {celsius_tmp:.2f}°C')
    print(f'maximum temperature in {city}: {celsius_tmp_max:.2f}°C')
    print(f'minimum temperature in {city}: {celsius_tmp_min:.2f}°C')
    print(f'weather description in {city}: {weather_description}')
    print(f'sunrise in {city} at {sunrise[0]} local time')
    print(f'sunset in {city} at {sunset[0]} local time')


def main():
    city = input("city : ")
    lat, lon = get_lat_lon(city)
    print_weather_data(get_weather(lat, lon), city)


if __name__ == '__main__':
    main()


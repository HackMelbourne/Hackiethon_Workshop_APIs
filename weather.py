import configparser
import requests
import sys
import calendar
from pprint import pprint
from datetime import date

def get_config():
	c = configparser.ConfigParser()
	c.read('config.ini')
	return [c['openweathermap']['api'], c['openweathermap']['city_id']]



def get_weather(api_key, city_id):
	url = "https://api.openweathermap.org/data/2.5/weather?id={}&appid={}&units=metric".format(city_id, api_key)
	r =requests.get(url)
	return r.json()

def main():
	
	config = get_config()
	api_key, city_id = config[0], config[1]
	weather = get_weather(api_key, city_id)

	pprint(weather)

	city_name = weather['name']
	current_temp = weather['main']['temp']
	description = weather['weather'][0]['description']
	
	print("It is {:.1f} today in {} and {}".format(current_temp, city_name, description))


if __name__ == '__main__':
	main()
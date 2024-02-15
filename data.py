import requests
from twilio.rest import Client
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

api_key = os.getenv('WEATHER_API_KEY')
auth_token = os.getenv('AUTH_TOKEN')
account_sid = os.getenv('ACCOUNT_SID')

# API Call Setup
open_weather_api_url ='https://api.openweathermap.org/data/2.5/forecast?'
parameters = {
    'appid': api_key,
    'lat': 45.421532,
    'lon': -75.697189,
    'units': 'metric',
    'cnt': 4
}
response = requests.get(open_weather_api_url,parameters )
response.raise_for_status()
data = response.json()

#inlcudes all the weather data. Eeach 3 hour perions is an element in the list
forcast_list = data['list']
#weather_condtions = forcast_list[0]['weather']

weather_id = []
weather_descr = []
#Ddate and times list
dt = []

for weather_condtions in forcast_list:
    weather_id.append(weather_condtions['weather'][0]['id'])
    weather_descr.append(weather_condtions['weather'][0]['description'])
    dt.append(weather_condtions['dt_txt'])

#Prints the weather conditions every 3 hours
for dt, weather in zip(dt,weather_descr):
    date, time = dt.split(' ')
    print(f"Date: {date}, Hour: {time}, Weather Condition: {weather}")

# Seding weather alerts uisng Twilio
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+17723616962',
    to='+16138900456',
    body = ' Fun fun Python '
)

print(message.status)
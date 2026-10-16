import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OWM_API_KEY")
auth_token = os.getenv("AUTH_TOKEN")

OWM_ENDPOINT = "http://api.openweathermap.org/data/2.5/forecast"


weather_params = {
    "lat": "45.764042",
    "lon": "4.835659",
    "q": "Lyon",
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json() 


#create a list of the condition codes spanning the next 12 hours
condition_codes = [forecast["weather"][0]["id"] for forecast in weather_data["list"]]

print(condition_codes)

#check if it will rain in the next 12 hours

will_rain = any(code < 700 for code in condition_codes)
if will_rain:
    print("Bring an Umbrella")
else:
    print("No need for an Umbrella")    

#create an environment variable called AUTH_TOKE
# Save the value of the auth_token under this environment variable.
#change the code to use the os module to retrieve the environment variables' value.
#run the main.py file to ensure that the program still works.
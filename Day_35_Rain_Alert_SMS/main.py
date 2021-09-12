import requests, os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient    # For using with PythonAnywhere to automate script

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"    # Openweathermap OneCall API (houly forecast for next 48hrs)
OWM_API = os.environ.get("OWM_API_KEY")     # In terminal, RUN "export OWM_API_KEY=<your_owm_api_key>"
account_sid = "<Twilio_Account_ID>"         
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")    # In terminal, RUN "export TWILIO_AUTH_TOKEN=<your_twilio_auth_token>"

# Latitude and Longitude for Singapore
MY_LAT = 1.352083
MY_LONG = 103.819839

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": OWM_API
}


# * Get hourly forecast for next 48 hours from https://openweathermap.org/
response = requests.get(OWM_ENDPOINT, params=weather_parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
# pprint.pprint(data)
hourly = weather_data["hourly"]
# pprint.pprint(hourly)

# * If script runs at 7am, just need the first 12 items from the list to cover from 7am-7pm
twelve_hours_forecast = hourly[:12]
# pprint.pprint(twelve_hours_forecast)

# * Look through 'id' in 'weather' in each of the 12 item to find anything below 700 (since anything below 700 is snow to rain)
weather_ids = [hour['weather'][0]['id'] for hour in twelve_hours_forecast if hour['weather'][0]['id'] < 700]
# print(weather_ids)

# * If 1 or more item means will rain, hence send SMS to remind user
if len(weather_ids) > 0:
    # print("Bring an umbrella")

    # ! Need the below code if using free account in PythonAnywhere https://www.pythonanywhere.com/ as they use proxy server for free tier
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}


    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages.create(body="It's going to rain today. Please remember to bring an ☔️umbrella☔️",
                                        from_="<Twilio_Number>",
                                            to="<Your_own_number>")
    
    print(message.status)   # To print message status
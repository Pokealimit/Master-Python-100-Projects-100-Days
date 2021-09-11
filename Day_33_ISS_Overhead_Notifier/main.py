import requests, smtplib, time
from datetime import datetime

# Latitude and Longitude for Singapore
MY_LAT = 1.352083 # Your latitude
MY_LONG = 103.819839 # Your longitude

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # * Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0, # To get ISO 8601 timing in order to compare with datetime output
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    # Splitting the ISO 8601 to get only the hour component
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_now_hr = time_now.hour


    # * Check if hour is more than sunset or less than sunrise
    if time_now_hr >= sunset or time_now_hr <= sunrise:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():

        my_email = "appbreweryinfo@gmail.com"
        password = "abcd1234()"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, 
                                to_addrs=my_email, 
                                msg=f"Subject:Look Up👆🏻 !\n\nThe ISS should be above you in the sky.")
        



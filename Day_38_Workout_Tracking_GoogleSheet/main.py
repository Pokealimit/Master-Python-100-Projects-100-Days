from decouple import config
import requests, pprint
from datetime import datetime


NUTRITIONIX_ID = config('NUTRITIONIX_ID')           # Alternatively, use os.getenv("")
NUTRITIONIX_APIKEY = config('NUTRITIONIX_APIKEY')
GENDER = config('GENDER')
HEIGHT = config('HEIGHT')
WEIGHT = config('WEIGHT')
AGE = config('AGE')
SHEETY_TOKEN = config('SHEETY_TOKEN')
WORKSHEET_ENDPOINT = config('WORKSHEET_ENDPOINT')

EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

HEADERS = {
    'x-app-id': NUTRITIONIX_ID,
    'x-app-key': NUTRITIONIX_APIKEY
}

exercises = input("Tell me which exercises you did: ").lower()

exercise_parameters = {
    "query": exercises,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_parameters, headers=HEADERS)
nutri_data = response.json()
pprint.pprint(nutri_data)

# * Retrieve name, duration_min and nf_calories information from nutri_data
exercise_list = [{"exercise": exercise['name'].title(), "calories": exercise['nf_calories'], "duration": exercise['duration_min']} for exercise in nutri_data['exercises']]
pprint.pprint(exercise_list)

sheety_auth_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}",
    "Content-Type": "application/json"
}

# * Get all the rows from the google worksheet
response = requests.get(url=WORKSHEET_ENDPOINT, headers=sheety_auth_headers)
response.raise_for_status()
worksheet_data = response.json()
pprint.pprint(worksheet_data)


# * Format today date and time to prep for input into google sheet
current = datetime.now()
only_date, only_time = current.date().strftime('%d/%m/%Y'), current.time().strftime("%H:%M:%S")
# only_date, only_time = current.date().strftime('%d/%m/%Y'), current.time().strftime("%X")
print(only_date)
print(only_time)


# * Adding Row to google worksheet using sheety
for exercise in exercise_list:
# for exercise in nutri_data['exercises']:

    sheety_row_data = {
        "workouts": {
            "date": only_date,
            "time": only_time,
            "exercise": exercise['exercise'],
            "duration": str(exercise['duration']),
            "calories": str(exercise['calories'])
        }
    }

    # sheety_row_data = {
    #     "workouts": {
    #         "date": only_date,
    #         "time": only_time,
    #         "exercise": exercise["name"].title(),
    #         "duration": exercise["duration_min"],
    #         "calories": exercise["nf_calories"]
    #     }
    # }


    response = requests.post(url=WORKSHEET_ENDPOINT, json=sheety_row_data, headers=sheety_auth_headers)
    response.raise_for_status()

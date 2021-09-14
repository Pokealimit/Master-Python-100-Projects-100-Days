import requests
from decouple import config
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = config('TOKEN')
USERNAME = config('USERNAME')
GRAPHS_ID = "graph1"

user_params = {
    "token": TOKEN,                 # Validation rule: [ -~]{8,128}
    "username": USERNAME,           # Validation rule: [a-z][a-z0-9-]{1,32}
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}

# * Create new user account (Execute once)
# response = requests.post(PIXELA_ENDPOINT, json=user_params)
# print(response.text)





GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPHS_ID,                # Validation rule: ^[a-z][a-z0-9-]{1,16}
    "name": "Cycling Graph",
    "unit": "Km",                   # Ex. commit, kilogram, calory.
    "type": "float",                # Only int or float are supported.
    "color": "ajisai"               # shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind
}

HEADERS = {
    "X-USER-TOKEN": TOKEN
}

# * Create new cycling graph (https://pixe.la/v1/users/pokealimit/graphs/graph1.html)
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
# print(response.text)






POST_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHS_ID}"

# Get today date in yyyyMMdd format using string of time
date = datetime.today().strftime('%Y%m%d')
# print(date)
# quantity = "10.4"
quantity = input("How many kilometres did you cycle today?: ")

pixel_data = {
    "date": date,
    "quantity": quantity
}

# * Post pixel to graph for today's date
response = requests.post(url=POST_PIXEL_ENDPOINT, json=pixel_data, headers=HEADERS)
print(response.text)





update_date = date      # For now
update_quantity = 15.4

UPDATE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHS_ID}/{update_date}"

update_pixel_data = {
    "quantity": str(update_quantity)
}

# * To update specified pixel  (if doesn't exist will create one)
# response = requests.put(url=UPDATE_PIXEL_ENDPOINT, json=update_pixel_data, headers=HEADERS)
# print(response.text)






delete_date = "20210914"

DELETE_PIXEL_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPHS_ID}/{delete_date}"

# * To delete specified pixel
# response = requests.delete(url=DELETE_PIXEL_ENDPOINT, headers=HEADERS)
# print(response.text)
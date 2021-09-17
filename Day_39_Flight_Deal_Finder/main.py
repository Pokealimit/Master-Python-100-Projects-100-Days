#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from decouple import config
from datetime import datetime, timedelta

SHEETY_TOKEN = config("SHEETY_TOKEN")
TEQUILA_API_KEY = config("TEQUILA_API_KEY")
ORIGIN_CITY_IATA = "SIN"

data_manager = DataManager(token=SHEETY_TOKEN)
flight_search = FlightSearch(apikey=TEQUILA_API_KEY)
notification_manager = NotificationManager()

sheet_data = data_manager.get_sheet_data()

pprint(sheet_data)


update = False
for flight in sheet_data:
    if not flight['iataCode']:
        flight['iataCode'] = flight_search.get_destination_code(flight['city'])
        update = True

if update:
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

# flight = flight_search.check_flights(origin_city_code=ORIGIN_CITY_IATA, destination_city_code="AKL", from_time=tomorrow, to_time=six_month_from_today, curr="SGD")
# pprint(flight)

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        curr="SGD"
    )

    if flight is not None:
        if flight.price < destination['lowestPrice']:
            notification_manager.send_email(
                message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            )








# [{'city': 'Paris', 'iataCode': 'PAR', 'id': 2, 'lowestPrice': 54},
#  {'city': 'Berlin', 'iataCode': 'BER', 'id': 3, 'lowestPrice': 42},
#  {'city': 'Tokyo', 'iataCode': 'TYO', 'id': 4, 'lowestPrice': 485},
#  {'city': 'Sydney', 'iataCode': 'SYD', 'id': 5, 'lowestPrice': 551},
#  {'city': 'Istanbul', 'iataCode': 'IST', 'id': 6, 'lowestPrice': 95},
#  {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'id': 7, 'lowestPrice': 414},
#  {'city': 'New York', 'iataCode': 'NYC', 'id': 8, 'lowestPrice': 240},
#  {'city': 'San Francisco', 'iataCode': 'SFO', 'id': 9, 'lowestPrice': 260},
#  {'city': 'Cape Town', 'iataCode': 'CPT', 'id': 10, 'lowestPrice': 378},
#  {'city': 'New Zealand', 'iataCode': '', 'id': 11, 'lowestPrice': 1900}]
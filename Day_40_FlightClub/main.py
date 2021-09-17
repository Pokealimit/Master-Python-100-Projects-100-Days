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
            users = data_manager.get_customer_emails()
            # pprint(users)
            emails = [row['email'] for row in users]
            names = [row['firstName'] for row in users]
            message=f"Low price alert! Only ${flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."

            # If there is stop_over
            if flight.stop_overs > 0:
                message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."
                print(message)
            
            # Send google flight link as well
            link = f"https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}"

            notification_manager.send_customer_emails(emails, message, link)








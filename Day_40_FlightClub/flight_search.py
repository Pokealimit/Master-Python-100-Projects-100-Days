from pprint import pprint
from flight_data import FlightData
import requests

TEQUILA_BASE_URL = "https://tequila-api.kiwi.com"
class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self, apikey:str):
        self.apikey = apikey
        self.headers = {
            "apikey": self.apikey
        }


    def get_destination_code(self, city_name: str):
        query = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(url=f"{TEQUILA_BASE_URL}/locations/query", params=query, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        pprint(data)
        return data['locations'][0]['code']


    def check_flights(self, origin_city_code:str, destination_city_code:str, from_time:str, to_time:str, curr:str):
        query = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": curr
        }

        response = requests.get(url=f"{TEQUILA_BASE_URL}/v2/search", params=query, headers=self.headers)
        # pprint(response.json())

        # ! Might not always get flight
        try:
            data = response.json()["data"][0]

        except IndexError:
            # Try again to find one with 1 stopover flight
            query["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_BASE_URL}/v2/search", headers=self.headers, params=query)
            # ! Might not always get flight as well
            try:
                data = response.json()["data"][0]

            except IndexError:
                print(f"No flights found for {destination_city_code}.")
                return None
            
            else:
                pprint(data)
                flight_data = FlightData(
                    price=data["price"],
                    origin_city=data["route"][0]["cityFrom"],
                    origin_airport=data["route"][0]["flyFrom"],
                    destination_city=data["route"][1]["cityTo"],
                    destination_airport=data["route"][1]["flyTo"],
                    out_date=data["route"][0]["local_departure"].split("T")[0],
                    return_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )
        
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
        
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data
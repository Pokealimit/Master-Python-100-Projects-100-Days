import requests

SHEETY_ENDPOINT = "https://api.sheety.co/9e8021f010a267fe0f7f58a629d9587a/flightDeals/prices"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, token: str) -> None:
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
        self.destination_data = {}

    def get_sheet_data(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]

        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.headers
            )
            print(response.text)
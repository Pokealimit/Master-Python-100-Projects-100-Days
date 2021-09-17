import requests

SHEETY_ENDPOINT = "https://api.sheety.co/9e8021f010a267fe0f7f58a629d9587a/flightDeals/users"

class UserManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self, token: str) -> None:
        self.headers = {
            "Authorization": f"Bearer {token}"
        }
    
    def add_user(self, first_name:str, last_name:str, email:str) -> bool:
        new_user ={
            "user": {
                "firstName": first_name,
                "lastName": last_name,
                "email": email
            }
        }
        response = requests.post(url=SHEETY_ENDPOINT, json=new_user, headers=self.headers)
        response.raise_for_status()
        print(response.status_code)
        if 200 <= response.status_code <= 299:
            return True
        else:
            return False
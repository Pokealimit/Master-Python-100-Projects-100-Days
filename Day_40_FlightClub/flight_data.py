class FlightData:
    def __init__(self, price:int, origin_city:str, origin_airport:str, destination_city:str, destination_airport:str, out_date:str, return_date:str, stop_overs:int=0, via_city:str=""):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

        self.stop_overs = stop_overs
        self.via_city = via_city
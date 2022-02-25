# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This class is responsible for talking to the Google Sheet.
from pprint import pprint

import requests

SHEETY_ENDPOINT = "https://api.sheety.co/4e12ce3dfb8293152e16533fafb5bf29/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        # use sheety api to get all the data in the Google sheet and print it out
        sheety_get_response = requests.get(url=SHEETY_ENDPOINT)
        sheety_get_response.raise_for_status()
        data = sheety_get_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"],
                }
            }
            print(new_data)
            sheety_put_response = requests.put(url=f"{SHEETY_ENDPOINT}/{city['id']}", json=new_data)
            sheety_put_response.raise_for_status()
            print(sheety_put_response.text)

# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This class is responsible for talking to the Flight Search API.

import os
import requests
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API = os.environ["TEQUILA_API_KEY"]


class FlightSearch:
    # def __init__(self):
    #     self.get_destination_code()

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        header = {
            "apikey": TEQUILA_API,
        }
        query = {
            "term": city_name,
            "location_types": "city",
        }

        response = requests.get(url=location_endpoint, params=query, headers=header)
        response.raise_for_status()
        # print(response)
        destination_data = response.json()["locations"]
        code = destination_data[0]["code"]
        return code

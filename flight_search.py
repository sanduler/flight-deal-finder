# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This class is responsible for talking to the Flight Search API.

import os
import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API = os.environ["TEQUILA_API_KEY"]
MIN_LENGTH_OF_STAY = 1
MAX_LENGTH_OF_STAY = 20
ADULTS = 2
MAX_STOPOVERS = 4


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

    def check_flight(self, origin_code, destination_code, from_time, to_time):
        header = {
            "apikey": TEQUILA_API
        }

        query = {
            "fly_from": origin_code,
            "fly_to": destination_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": MIN_LENGTH_OF_STAY,
            "nights_in_dst_to": MAX_LENGTH_OF_STAY,
            "flight_type": "round",
            "one_for_city": 1,
            "adults": ADULTS,
            "max_stopovers": MAX_STOPOVERS,
            "curr": "USD",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=query, headers=header)

        # take account the not flights edge case
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_code}.")
            return None

        flight_data = FlightData()
        flight_data.price = data["price"]
        flight_data.origin_city = data["route"][0]["cityFrom"]
        flight_data.origin_airport = data["route"][0]["flyFrom"]
        flight_data.destination_city = data["route"][0]["cityTo"]
        flight_data.destination_airport = data["route"][0]["flyTo"]
        flight_data.out_date = data["route"][0]["local_departure"].split("T")[0]
        flight_data.return_date = data["route"][1]["local_departure"].split("T")[0]

        print(f"{flight_data.destination_city}: ${flight_data.price}")

        return flight_data

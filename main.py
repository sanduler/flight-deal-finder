# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This program uses the DataManager,FlightSearch, FlightData, NotificationManager classes to
#              achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

ORIGIN_CITY ="PDX"

data_managing = DataManager()
sheet_data = data_managing.get_destination_data()
flight_searching = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_searching.get_destination_code(row["city"])
        # print(f"sheet_data:\n {sheet_data}")

    data_managing.destination_data = sheet_data
    data_managing.update_destination_codes()


# start the search from next day --> tomorrow
tomorrow = datetime.now() + timedelta(days=1)
# look into the future six months --> 6 months = 30 * 6 months
six_months = datetime.now() + timedelta(days=(6*30))

# look into each of the destination codes to search for the flight
for destination in sheet_data:
    pass
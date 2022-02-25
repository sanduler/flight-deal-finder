# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This program uses the DataManager,FlightSearch, FlightData, NotificationManager classes to
#              achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch

data_managing = DataManager()
sheet_data = data_managing.get_destination_data()
# print(sheet_data)

flight_searching = FlightSearch()

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_searching.get_destination_code(row["city"])
        # print(f"sheet_data:\n {sheet_data}")

    data_managing.destination_data = sheet_data
    data_managing.update_destination_codes()


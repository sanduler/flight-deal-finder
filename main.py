# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This program uses the DataManager,FlightSearch, FlightData, NotificationManager classes to
#              achieve the program requirements.
import json
import os
from twilio.rest import Client

import requests

# account_sid = os.environ["TWILIO_ACCOUNT_SID"]
# auth_token = os.environ["TWILIO_AUTH_TOKEN"]
# FROM_PHONE = os.environ["FROM_TEXT"]
# TO_PHONE = os.environ["TO_TEXT"]
#
# # bool tag do we need an ubreala? No
# bring_umbrella = False
#
# # twilio API implementation send a text automaticly if it will rain
# if bring_umbrella:
#     client = Client(account_sid, auth_token)
#     message = client.messages \
#         .create(
#         body="It's going to rain today! Don't forget to bring an Umbrella ☂️ ☂",
#         from_=FROM_PHONE,
#         to=TO_PHONE
#     )
#
# # print the status once the text is sent.
# print(message.status)
sheety_endpoint = "https://api.sheety.co/4e12ce3dfb8293152e16533fafb5bf29/flightDeals/prices/2"
sheety_get_response = requests.get(url=sheety_endpoint)
sheety_get_response.raise_for_status()
data = sheety_get_response.json()
print(data)
# sheety_response = requests.put(url=sheety_endpoint)
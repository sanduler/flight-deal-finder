# Name: Ruben Sanduleac
# Date: 02/24/22
# Description: This class is responsible for sending notifications with the deal flight details.

from twilio.rest import Client
import os

TWILIO_SID = os.environ["TWILIO_ACCOUNT_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]
TWILIO_VIRTUAL_NUMBER = os.environ["FROM_TEXT"]
TWILIO_VERIFIED_NUMBER = os.environ["TO_TEXT"]


class NotificationManager:
    """This class is responsible for notifying the user
    The class uses Twilio API to send the user a text about the
     lowest flight deal to date."""
    def __init__(self):
        """Prototype which always initializes the token and the if from Twilio"""
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """send_sms function is responsible for the message that is sent to the user from a varified
         phone number to a verified phone"""
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        # print(message.sid)

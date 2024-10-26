import pandas as pd
from datetime import datetime, timedelta
from twilio.rest import Client

class Class:
    def __init__(self, day, timing, professor_number, class_subject):
        self.day = day
        self.timing = timing
        self.professor_number = professor_number
        self.class_subject = class_subject

class NotificationSystem:
    def __init__(self, class_routine, account_sid, auth_token, twilio_phone_number):
        self.class_routine = class_routine
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_phone_number = twilio_phone_number

    def send_notification(self, professor_number, class_subject, timing):
        client = Client(self.account_sid, self.auth_token)

        # Format the message
        message_body = f"Reminder: You have a class of {class_subject} starting in 1 minute at {timing}."

        # Send message using Twilio
        message = client.messages.create(
            body=message_body,
            from_=self.twilio_phone_number,
            to=professor_number
        )

        print(f"Notification sent to {professor_number}: {message.sid}")

    def check_and_send_notifications(self):
        current_day = datetime.now().strftime("%A")
        current_time = datetime.now()

        for class_info in self.class_routine:
            class_day = class_info.day
            class_time = datetime.strptime(class_info.timing, "%I:%M-%p")

            # Calculate time difference
            time_difference = class_time - current_time

            # If the class is today and the time difference is exactly 1 minute
            if class_day == current_day and timedelta(minutes=1) <= time_difference < timedelta(minutes=2):
                self.send_notification(class_info.professor_number, class_info.class_subject, class_info.timing)

if __name__ == "__main__":
    # Twilio credentials
    account_sid = "your_account_sid"
    auth_token = "your_auth_token"
    twilio_phone_number = "your_twilio_phone_number"

    # list to store class objects
    class_routine = [
        Class("Sunday", "6:35-7:10", "+1234567890", "Phy(BDG)"),
        #ajhai baaki cha aru add garna
        #excel bata file routine file import garera is also nice
    ]

    notification_system = NotificationSystem(class_routine, account_sid, auth_token, twilio_phone_number)
    notification_system.check_and_send_notifications()

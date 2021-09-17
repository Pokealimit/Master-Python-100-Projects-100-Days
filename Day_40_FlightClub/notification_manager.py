from twilio.rest import Client
from decouple import config
import smtplib
from email.message import EmailMessage

# TWILIO_SID = config('TWILIO_SID')
# TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
# TWILIO_VIRTUAL_NUMBER = config('TWILIO_VIRTUAL_NUMBER')
# TWILIO_VERIFIED_NUMBER = config('TWILIO_VERIFIED_NUMBER')

SENDER_GMAIL = config('SENDER_GMAIL')
SENDER_PASSWORD = config('SENDER_PASSWORD')
RECEIVER_EMAIL = config('RECEIVER_EMAIL')

class NotificationManager:

    def __init__(self):
        # self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        pass

    # def send_sms(self, message):
    #     message = self.client.messages.create(
    #         body=message,
    #         from_=TWILIO_VIRTUAL_NUMBER,
    #         to=TWILIO_VERIFIED_NUMBER,
    #     )
    #     # Prints if successfully sent.
    #     print(message.sid)

    def send_email(self, message):
        em = EmailMessage()
        em.set_content(message)
        em['To'] = RECEIVER_EMAIL
        em['From'] = SENDER_GMAIL
        em['Subject'] = "Flight Price Alert!"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_GMAIL, password=SENDER_PASSWORD)
            # connection.sendmail(from_addr=SENDER_GMAIL, 
            #                     to_addrs=RECEIVER_EMAIL, 
            #                     msg=f"Subject:Flight Price Alert!\n\n{message}")
            connection.send_message(em)

    def send_customer_emails(self, emails, message, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SENDER_GMAIL, password=SENDER_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=SENDER_GMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
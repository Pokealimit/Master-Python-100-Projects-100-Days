import smtplib
import datetime as dt
from random import choice

# Set up smtp
my_email = "appbreweryinfo@gmail.com"
password = "abcd1234()"

# * Get current day of the week
day_of_week = dt.datetime.now().weekday()
# print(day_of_week)

# Check if day_of_week is monday
if day_of_week == 0:
    # * Open quotes.txt
    with open("quotes.txt", "r") as quotes_file:
        quotes = quotes_file.readlines()
        quotes = [quote.replace('\n', "") for quote in quotes]
        quotes = [quote.replace('\'', "") for quote in quotes]

    quote = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs="appbrewerytesting@yahoo.com", 
                            msg=f"Subject:Motivational Quote\n\n{quote}")


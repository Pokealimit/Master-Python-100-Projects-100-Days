##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }

import pandas as pd
df = pd.read_csv("birthdays.csv", index_col="name")
print(df)
birthdays_dict = { (row.month,row.day) : (index, row.email) for (index, row) in df.iterrows() }
# print(birthdays_dict)

#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

import datetime as dt
current_date = dt.datetime.now()
current_month = current_date.month
current_day = current_date.day
# print((current_month, current_day))


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp
from random import choice
import smtplib

if (current_month, current_day) in birthdays_dict:
    # print(birthdays_dict[(current_month, current_day)])
    birthday_name = birthdays_dict[(current_month, current_day)][0]
    birthday_email = birthdays_dict[(current_month, current_day)][1]

    letter_list = ("letter_1.txt", "letter_2.txt", "letter_3.txt")
    letter = choice(letter_list)
    # print(letter)

    with open(file=f"letter_templates/{letter}", mode="r") as template:
        customised_template = template.read().replace("[NAME]", birthday_name)
        # print(customised_template)
        # print(birthday_email)

    # 4. Send the letter generated in step 3 to that person's email address.
    # HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

    my_email = "appbreweryinfo@gmail.com"
    password = "abcd1234()"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, 
                            to_addrs=birthday_email, 
                            msg=f"Subject:Happy Birthday {birthday_name}!\n\n{customised_template}")

import smtplib

#! Need to enable less secure apps on mail server
my_email = "appbreweryinfo@gmail.com"
password = "abcd1234()"

# * for gmail is "smtp.gmail.com" but for yahoo is "smtp.mail.com" (Need to check smtp info)
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, 
                        to_addrs="appbrewerytesting@yahoo.com", 
                        msg="Subject:Hello\n\nThis is the body of my email")

# connection.close() # * redundant with using "with X as x: "
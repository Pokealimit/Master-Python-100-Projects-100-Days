from decouple import config
from user_manager import UserManager

SHEETY_TOKEN = config("SHEETY_TOKEN")


if __name__ == "__main__":

    user_manager = UserManager(token=SHEETY_TOKEN)


    print("Welcome to David's Flight Club.\nWe'll find the best flight deals and email you.")
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    # Ask email twice for verification
    email_1 = input("What is your email?\n")
    email_2 = input("Type your email again.\n")

    if email_1 == email_2:
        if user_manager.add_user(first_name=first_name, last_name=last_name, email=email_1):
            print("Congrats! You're in the club!")
        else:
            print("Failed to add")
    else:
        print("Sorry. The email address you have input does not match.\nPlease try again.")



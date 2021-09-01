from turtle import pen
from matplotlib import offsetbox


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def check_user_input():
    usr_input = input("What would you like? (espresso/latte/cappuccino): ")
    return usr_input

# def print_report(water, milk, coffee, money):
#     print(f"Water: {water}ml")
#     print(f"Milk: {milk}ml")
#     print(f"Coffee: {coffee}g")
#     print(f"Money: ${money:.2f}")

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']:.2f}")

def order_drink(choice):
    for ingredient in MENU[choice]['ingredients']:
        if  resources[ingredient] < MENU[choice]['ingredients'][ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return
    if process_coin(choice):
        # print(f"report before purchasing {choice}")
        # print_report()
        for ingredient in MENU[choice]['ingredients']:
            resources[ingredient] -= MENU[choice]['ingredients'][ingredient]
        resources["money"] += MENU[choice]['cost']
        # print(f"report after purchasing {choice}")
        # print_report()
        print(f"Here is your {choice}. Enjoy!")

def process_coin(choice):
    quarters = input("Input no. of quarters: ")
    dimes = input("Input no. of dimes: ")
    nickles = input("Input no. of nickle: ")
    pennies = input("Input no. of pennies: ")
    total = int(quarters)*0.25 + int(dimes)*0.1 + int(nickles)*0.05 + int(pennies)*0.01
    if total < MENU[choice]['cost']:
        print("Sorry, that's not enough money. Money refunded.")
        return False
    elif total > MENU[choice]['cost']:
        refund = total - MENU[choice]['cost']
        print(f"Too much money, refunding change of ${refund:.2f}")
        return True
    else:
        return True


if __name__ == "__main__":

    while True:
        choice = check_user_input()

        try:
            if MENU[choice]:
                order_drink(choice)

        except:

            if choice == 'off':
                break
            elif choice == 'report':
                print_report()
            else:
                print('invalid input, try again')


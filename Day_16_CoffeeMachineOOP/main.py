from http.cookies import CookieError
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

if __name__ == "__main__":
    # Creating Objects
    menu = Menu()
    coffeemaker = CoffeeMaker()
    cashier = MoneyMachine()

    while True:
        # Get user input
        usr_input = input(f"What would you like? ({menu.get_items()}):")
        if usr_input == 'report':
            # Report current status
            coffeemaker.report()
            cashier.report()
        elif usr_input == 'off':
            # Turn off machine
            break
        # check if drink is an object
        else:
            try:
                drink = menu.find_drink(usr_input)
                # check if sufficient ingredients for drink
                if coffeemaker.is_resource_sufficient(drink):
                    # User to make payment
                    if (cashier.make_payment(drink.cost)):
                        coffeemaker.make_coffee(drink)
            except:
                pass

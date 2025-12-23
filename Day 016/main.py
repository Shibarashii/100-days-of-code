from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    coffee_maker.report()
    money_machine.report()

    menu_items = menu.get_items()
    choice = input(f"What would you like? {menu_items}")

    drink = menu.find_drink(choice)

    if coffee_maker.is_resource_sufficient(drink):
        payment_success = money_machine.make_payment(drink.cost)

        if payment_success:
            coffee_maker.make_coffee(drink)

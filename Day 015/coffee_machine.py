# In dollars
QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01


resources = {
    "water": 300,  # ml
    "milk": 200,   # ml
    "coffee": 100,  # g
    "money": 0  # $
}

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


def valid_transaction(_choice, _payment):
    return _payment >= MENU[_choice]["cost"]


def insert_coins():
    print("Please insert coins.")

    quarters_total = int(input("How many quarters?: ")) * QUARTER
    dimes_total = int(input("How many dimes?: ")) * DIME
    nickles_total = int(input("How many nickles?: ")) * NICKLE
    pennies_total = int(input("How many pennies?: ")) * PENNY

    total = quarters_total + dimes_total + nickles_total + pennies_total

    return total


def resources_sufficient(_choice):
    sufficient_water = resources["water"] >= MENU[_choice]["ingredients"]["water"]
    sufficient_coffee = resources["coffee"] >= MENU[_choice]["ingredients"]["coffee"]
    sufficient_milk = resources["milk"] >= MENU[_choice]["ingredients"]["milk"] if _choice != "espresso" else True
    return sufficient_water and sufficient_coffee and sufficient_milk


def calculate_transaction(_choice, _total_payment):
    resources["water"] -= MENU[_choice]["ingredients"]["water"]
    resources["milk"] -= MENU[_choice]["ingredients"]["milk"] if _choice != "espresso" else 0
    resources["coffee"] -= MENU[_choice]["ingredients"]["coffee"]
    resources["money"] += MENU[_choice]["cost"]

    change = _total_payment - MENU[_choice]["cost"]

    return change


def start_coffee_machine():
    report = (f"""
    Water: {resources["water"]}ml
    Milk: {resources["milk"]}ml
    Coffee: {resources["coffee"]}g
    Money: ${resources["money"]}
    """)

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice not in ["espresso", "latte", "cappuccino", "report"]:
            print("Please choose a valid option")
        else:
            break

    if choice == "report":
        print(report)

    elif not resources_sufficient(choice):
        print("Sorry, not enough resources")
        print(report)

    else:
        total_payment = insert_coins()

        if valid_transaction(choice, total_payment):
            change = calculate_transaction(choice, total_payment)

            print(f"Here is ${change:.2f} in change.")
            print(f"Enjoy your {choice}")

        else:
            print("Sorry, that's not enough money.")
            start_coffee_machine()


while True:
    start_coffee_machine()

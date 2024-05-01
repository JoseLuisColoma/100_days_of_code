from data import *

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01


def report():
    """Returns True when order can be made, False if ingredients are insufficient."""
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {round(profit['value'], 2)}€")


def check_resources(coffee_choice):
    is_enough = True
    if MENU[coffee_choice]['ingredients']['water'] > resources['water']:
        print(f"There isn't enough water for a {coffee_choice}.")
        is_enough = False
    if MENU[coffee_choice]['ingredients']['coffee'] > resources['coffee']:
        print(f"There isn't enough coffee for a {coffee_choice}.")
        is_enough = False
    if coffee_choice != 'espresso':
        if MENU[coffee_choice]['ingredients']['milk'] > resources['milk']:
            print(f"There isn't enough milk for a {coffee_choice}.")
            is_enough = False
    return is_enough


def process_coins(quarter, dime, nickle, penny):
    """ Returns the total calculated from coins inserted """
    quarter *= QUARTER
    dime *= DIME
    nickle *= NICKLE
    penny *= PENNY
    total = quarter + dime + nickle + penny
    return total


def deduct_resources(coffee_choice):
    resources['water'] -= MENU[coffee_choice]['ingredients']['water']
    resources['coffee'] -= MENU[coffee_choice]['ingredients']['coffee']
    if coffee_choice != 'espresso':
        resources['milk'] -= MENU[coffee_choice]['ingredients']['milk']


def coffee_machine():
    is_on = True
    while is_on:
        choice = input("What would you like? Type 'espresso', 'latte', 'cappuccino': ").lower()
        if choice == 'report':
            report()
            coffee_machine()
        elif choice == 'off':
            print("Turning off.")
            is_on = False
        elif check_resources(choice):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            if process_coins(quarters, dimes, nickles, pennies) == MENU[choice]['cost']:
                deduct_resources(choice)
                profit['value'] += MENU[choice]['cost']
                print(f"Here is your {choice} ☕. Have a good one!")
            elif process_coins(quarters, dimes, nickles, pennies) > MENU[choice]['cost']:
                deduct_resources(choice)
                profit['value'] += MENU[choice]['cost']
                change = process_coins(quarters, dimes, nickles, pennies) - MENU[choice]['cost']
                change = round(change, 2)
                print(f"Here is ${change} in change.")
                print(f"Here is your {choice} ☕. Have a good one!")
            else:
                print(f"Not enough money, ${(process_coins(quarters, dimes, nickles, pennies))} refunded.")


coffee_machine()

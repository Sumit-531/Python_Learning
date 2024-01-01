from menu import MENU, resources

# TODO: 1. Asking user for their coffee

# TODO: 2. Turn off the coffee machine if the user enter "Off"


def coffee_machine_shutdown(decision):
    """This function shutdown the coffee machine when user type off"""
    if user_decision == "off":
        return "Thank you!"


# TODO: 3. Print a report


def remaining_resource(coffe_choice, element):
    """This function shows the report"""
    # if coffe_choice == "latte" or coffe_choice == "espresso" or coffe_choice == "cappuccino":
    water = resources['water'] - MENU[coffe_choice]["ingredients"]["water"]
    milk = resources['milk'] - MENU[coffe_choice]["ingredients"]["milk"]
    coffee = resources['coffee'] - MENU[coffe_choice]["ingredients"]["coffee"]

    if element == "every":
        return f"Water: {water}\nMilk: {milk}\nCoffee: {coffee}g"
    elif element == "water":
        return water
    elif element == "milk":
        return milk
    elif element == "coffee":
        return coffee

# def can_order(n_water, n_milk, n_coffee):
#     if n_milk < 150 or n_water < 200 or n_coffee < 24:
#         return "no"
def coin():
    """This function ask for the coins and then return total amount"""
    print("Please insert coin.")
    quarter = int(input("how many quarters? :"))
    dime = int(input("how many dimes? :"))
    nickel = int(input("how many nickels? :"))
    penni = int(input("how many pennies? :"))

    money = (quarter * 0.25) + (dime * 0.10) + (nickel * 0.05) + (penni * 0.01)
    return money


def first_report():
    water_one = resources['water']
    milk_two = resources['milk']
    coffee_three = resources['coffee']
    return f"Water: {water_one}\nMilk: {milk_two}\nCoffee: {coffee_three}g"


def transaction(user_money, coffee_price):
    """This function takes user money and the coffee price as input"""
    if user_money < coffee_price:
        user_money = "{:.2f}".format(user_money)
        # return f"Sorry that's not enough money. ${user_money} refunded."
        return user_money
    elif user_money > coffee_price:
        change_money = user_money - coffee_price
        change_money = "{:.2f}".format(change_money)
        # return f"Here is ${change_money} in change.\nHere is your {coffee_type} ☕. Enjoy!"
        return change_money


is_ordered = False
should_continue = True
while should_continue:
    # if user print first report then
    user_decision = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # water = remaining_resource("latte", "water")
    # print(water)
    # milk = remaining_resource("latte", "milk")
    # print(milk)
    # coffee = remaining_resource("latte", "coffee")
    # print(coffee)

    if user_decision == "off":
        print(coffee_machine_shutdown("off"))

    elif user_decision == "latte":
        total_money = (coin())
        process_coin = transaction(total_money, 2.5)
        if total_money < 2.5:
            print(f"Sorry that's not enough money. ${process_coin} refunded.")
        elif total_money > 2.5:
            rem = remaining_resource("latte", "every")
            is_ordered = True
            print(f"Here is ${process_coin} in change.\nHere is your latte ☕. Enjoy!")

    elif user_decision == "espresso":
        total_money = (coin())
        process_coin = transaction(total_money, 1.5)
        if total_money < 1.5:
            print(f"Sorry that's not enough money. ${process_coin} refunded.")
        elif total_money > 1.5:
            # if not can_order(water, milk, coffee):
            #     print("Sorry insufficient ingredients")
            #     print(f"Sorry that's not enough money. ${process_coin} refunded.")
            # else:
            rem = remaining_resource("espresso", "every")
            is_ordered = True
            print(f"Here is ${process_coin} in change.\nHere is your espresso ☕. Enjoy!")

    elif user_decision == "cappuccino":
        total_money = (coin())
        process_coin = transaction(total_money, 3.0)
        if total_money < 3.0:
            print(f"Sorry that's not enough money. ${process_coin} refunded.")
        elif total_money > 3.0:
            # if not can_order(water, milk, coffee):
            #     print("Sorry insufficient ingredients")
            #     print(f"Sorry that's not enough money. ${process_coin} refunded.")
            # else:
            rem = remaining_resource("cappuccino", "every")
            is_ordered = True
            print(f"Here is ${process_coin} in change.\nHere is your cappuccino ☕. Enjoy!")

    elif user_decision == "report":
        if not is_ordered:
            print(first_report())
        elif is_ordered:
            print(rem)

    else:
        print("Invalid input")
        
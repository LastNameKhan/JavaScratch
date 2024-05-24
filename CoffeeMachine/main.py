from machine_data import MENU
from machine_data import resources

order_again = False


def calculate_total():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    pennies = int(input("How many pennies?: "))
    nickles = int(input("How many nickles?: "))
    customer_money = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    return customer_money


def customer_selection():
    global order_again
    user_input = input("What would you like?(espresso/latte/cappuccino): ")
    latte_cost = MENU["latte"]["cost"]
    espresso_cost = MENU["espresso"]["cost"]
    cappuccino_cost = MENU["cappuccino"]["cost"]
    if user_input == 'latte':
        total_money_by_user = round(calculate_total(), 2)
        if total_money_by_user >= latte_cost and resources["water"] > 200 and resources["milk"] > 150:
            if resources["coffee"] > 24:
                customer_change = total_money_by_user - latte_cost
                resources["water"] = resources["water"] - MENU["latte"]["ingredients"]["water"]
                resources["milk"] = resources['milk'] - MENU["latte"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                print(f"Here is your ${customer_change} in change.")
                print("Here is your latte. Enjoy!!")
            else:
                order_again = True
        else:
            order_again = True
    elif user_input == "espresso":
        total_money_by_user = round(calculate_total(), 2)
        if total_money_by_user >= espresso_cost and resources["water"] > 50 and resources["coffee"] > 18:
            customer_change = total_money_by_user - espresso_cost
            resources["water"] = resources["water"] - MENU["espresso"]["ingredients"]["water"]
            resources["coffee"] = resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
            print(f"Here is your ${customer_change} in change.")
            print("Here is your espresso. Enjoy!!")
        else:
            order_again = True
    elif user_input == "cappuccino":
        total_money_by_user = round(calculate_total(), 2)
        if total_money_by_user >= espresso_cost and resources["water"] > 250 and resources["milk"] > 100:
            if resources["coffee"] > 24:
                customer_change = total_money_by_user - cappuccino_cost
                resources["water"] = resources["water"] - MENU["cappuccino"]["ingredients"]["water"]
                resources["milk"] = resources['milk'] - MENU["cappuccino"]["ingredients"]["milk"]
                resources["coffee"] = resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                print(f"Here is your ${customer_change} in change.")
                print("Here is your cappuccino. Enjoy!!")
            else:
                order_again = True
        else:
            order_again = True

    elif user_input == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")


while not order_again:
    customer_selection()

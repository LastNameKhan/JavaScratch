from machine_data import MENU
from machine_data import resources

print(MENU)


def calculate_total(quarters, dimes, nickles, pennies):
    customer_money = float((quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01))
    return customer_money


def customer_selection():
    user_input = input("What would you like?(espresso/latte/cappuccino): ").lower()
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    pennies = int(input("How many pennies?: "))
    nickles = int(input("How many nickles?: "))
    total_money_by_user = round(calculate_total(quarters, dimes, nickles, pennies), 2)
    if user_input == 'latte' and total_money_by_user < MENU["latte"]["cost"]:
        customer_change = total_money_by_user - MENU["latte"]["cost"]
        
        print(f"Here is your ${customer_change} in change.")
    print(total_money_by_user)


customer_selection()

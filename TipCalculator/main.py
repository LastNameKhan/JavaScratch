print("Welcome to the Tip Calculator!")
initial_bill = float(input("What was the total bill? $ "))
tip = int(input("How much tip would you like to give? 10,12 or 15 ? "))
member = int(input("How many people are splitting the bill? "))

tip_amount = initial_bill * tip /100
total_bill = initial_bill + tip_amount
split_amount = round(total_bill / member,2)
print(f"Each person should pay {split_amount}")
print("Welcome to the Tip Calculator!")
initial_bill = input("What was the total bill? $ ")
int_bill = int(initial_bill)
print(int_bill*2)

tip = input("How much tip would you like to give? 10,12 or 15 ? ")
converted_total_tip = int(tip)

total_bill = (int_bill * 12)/100
# total_bill_with_tip = converted_total_tip%12
# member = input("How many people to split the bill?")
# tip_formula = total_bill_with_tip/member
# print(f"Each person should pay {tip_formula}")
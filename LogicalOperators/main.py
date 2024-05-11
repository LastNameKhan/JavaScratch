# A and B - Both have to be True else it will return False
# C or D - Id only needed one of the condition to be true
# not E It reverses the condition for example if any codition is true is reverses it to false and vice versa
print("Welcome to the RollerCoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("Can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")
    elif age >= 45 and age <= 55:
        print("Midlife Crisis Age Discount")
    else:
        bill = 12
        print("Please pay $12.") 
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your total bill is {bill}")
else:
    print("Can't ride the rollercoaster")
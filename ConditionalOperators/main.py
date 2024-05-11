# Operator and Meaning
# > Greater then
# < Less then
# >= Greter then or equal to
# <= Less then or equal to
# == Equal to
# != Not Equal to
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
    else:
        bill = 12
        print("Please pay $12.") 
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your total bill is {bill}")
else:
    print("Can't ride the rollercoaster")
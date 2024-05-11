# Operator and Meaning
# > Greater then
# < Less then
# >= Greter then or equal to
# <= Less then or equal to
# == Equal to
# != Not Equal to
print("Welcome to the RollerCoaster!")
height = int(input("What is your height in cm? "))
if height >= 120:
    print("Can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.") 
else:
    print("Can't ride the rollercoaster")
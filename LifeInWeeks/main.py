print("Welcome to Life in Weeks Calculator for refence the default age set that maximum a human can live is 90 years")
age = input("Please Enter your Age?\n")
print(age)
converted_age = int(age)
#Converting the years into weeks
convert_year_to_week = converted_age * 52
#Calcuating the Years remaining 
remaining_year = 90 - int(age)
#Calcualting the remaining weeks
remaining_weeks = remaining_year*int(52)
#Printing out the weeks left 
print(f"You have {remaining_weeks} weeks left.")
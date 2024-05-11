height = float(input())
weight = int(input())

height_expo = height ** 2
bmi_cal = weight/height_expo

if bmi_cal < 18.5:
    print(f"Your BMI is {bmi_cal}, you are underweight.")
elif bmi_cal < 25:
    print(f"Your BMI is {bmi_cal}, you have normal weight.")
elif bmi_cal < 30:
    print(f"Your BMI is {bmi_cal}, you are slightly overweight.")
elif bmi_cal < 35:
    print(f"Your BMI is {bmi_cal}, you are obese.")
else:
    print(f"Your BMI is {bmi_cal}, you are clinically obese.")

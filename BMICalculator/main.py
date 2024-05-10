# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

weight = input()
height = input()

#Converting the weight and height into int and float for the calculation

converted_height = float(height)
converted_weight = int(weight)
exponential_height = converted_height ** 2

final_bmi = converted_weight/exponential_height

print(int(final_bmi))
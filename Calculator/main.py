import art_module

print(art_module.logo)

# continuation_flag = False
# use_previous_result = False
# first_number = 0

# while not continuation_flag:
#     if not use_previous_result:
#         first_number = int(input("What's the first number?\n"))
    
#     second_number = int(input("What's the second number?\n"))
#     operation = ["+", "-", "*", "/"]
#     for items in operation:
#         print(items)
#     pick_operation = input("Pick an Operation: ")
    
#     if pick_operation == "+":
#         first_answer = first_number + second_number
#     elif pick_operation == "-":
#         first_answer = first_number - second_number
#     elif pick_operation == "*":
#         first_answer = first_number * second_number
#     elif pick_operation == "/":
#         first_answer = first_number / second_number
#     else:
#         print("Please select a Valid Operator!")
#         continue

#     print(f"Result: {first_answer}")
    
#     continuation = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to stop: ").lower()
#     if continuation == 'y':
#         first_number = first_answer
#         use_previous_result = True
#     elif continuation == 'n':
#         continuation_flag = True
#         use_previous_result = False

# Second Method
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 + n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = int(input("What's the first number?: "))
    for key in operations:
        print(key)
    continue_calculation = True

    while continue_calculation:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = int(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continue_check = input(f"Type 'y' or 'n' to continue further with {answer}")
        if continue_check == "y":
            num1 = answer
        else:
            continue_calculation = False
            calculator()


calculator()
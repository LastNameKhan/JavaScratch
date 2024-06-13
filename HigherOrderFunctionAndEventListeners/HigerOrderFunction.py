def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1/n2


def calculator(n1, n2, func):
    return func(n1, n2)


# Here Calculator is Higher Order Function
result = calculator(2, 3, multiply)
print(result)

# A function that can work with other function or it takes
# another function as an argument
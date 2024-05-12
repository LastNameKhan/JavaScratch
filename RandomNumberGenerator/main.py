import random
import my_module

# Generating random whole number 
a = int(input())
b = int(input())
random_integer_hardcoded = random.randint(10,15)
print(f"Hard Coded Random Integer is {random_integer_hardcoded}")
random_integer = random.randint(a,b)
print(random_integer)

# Using our own created module
print(my_module.pi)

# Generating random floating number
print(random.random())

# Generating a random number from 0 to any given integer
print(random.random() * 5)



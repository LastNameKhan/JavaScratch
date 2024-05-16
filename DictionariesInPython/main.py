# Syntax for the Dictioanry is
# {key: Value}

# example
programming_dictionary = {
    "Bug":"An Error in a program that prevents the program from running as expected",
    "Function":"A piece of code that you can easily call over and over again"
}

# Get any value from the dictionary by the name of the key
# We should call the correct datatype of the key here it is a string on other case make sure the key datatype is correct
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Create an empty distionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "This is an edited message"
print(programming_dictionary)

# Loop through an dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])
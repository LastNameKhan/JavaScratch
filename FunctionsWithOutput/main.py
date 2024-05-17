def my_function():
    result = 3 * 2
    # We can use the output keyword which is "return" in order to get the output from this function
    return result

output = my_function()
print(output)

first_name = input("What is your first name? ")
last_name = input("What is your Last name? ")
def format_name(f_name,l_name):
    # Multiple Return
    if f_name == "" or l_name == "":
        return
    return f"{f_name.title()} {l_name.title()}"

formatedName = format_name(first_name,last_name)
print(formatedName)

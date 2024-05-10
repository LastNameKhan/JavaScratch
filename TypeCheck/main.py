# len(4837)
# We will get an error from the above code which says that int does not support len or does not gave len()

num_char = len(input("What is your name?"))
# print("Your name has " + num_char + " characters")

# In the above code we will get an error which says can only concatenate string s not int to str to resolve it

#TypeCheck
print(type(num_char))

#TypeConversion
converted_num_char = str(num_char)
print("Your name has " + converted_num_char + " characters")


a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70)+ str(100))





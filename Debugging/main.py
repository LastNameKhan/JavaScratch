# Describe Problem
# def my_function():
#     # range deos not reach at the end it tracks index which starts from 0
#     for i in range(1,20):
#         if i == 20:
#             print("You got it")
# my_function()

# Reproduce the Bug
import random

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# When dice number return 6 we will get an error brcause of index issue
dice_num = random.randint(0, 5)
print(dice_imgs[dice_num])

# Play Computer
year = int(input("What's your year of birth?"))
# In the below code we have missing eqaul to condition for 1994 hence we need to correct it with equal to
if year > 1980 and year < 1994:
  print("You are a millenial.")
# Adding equal to sign
elif year >= 1994:
  print("You are a Gen Z.")


# Fix the Error
# We will get an Type error if we don't use the Type correctly hence int is important to store an integer
age = int(input("How old are you?"))
if age > 18:
  print(f"You can drive at age {age}.")

# Must use print to resolve the Bugs
#  If we use == then we check the data type not set the value 
# to assign the value we have to use single equal sign
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
print(pages)
word_per_page = int(input("Number of words per page: "))
print(word_per_page)
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)
    print(b_list)

mutate([1, 2, 3, 5, 8, 13])
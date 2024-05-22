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
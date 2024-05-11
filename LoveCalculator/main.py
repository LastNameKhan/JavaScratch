print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
conatenated_string = name1 + name2
num_count = 0
check_t = conatenated_string.lower().count("t")
check_r = conatenated_string.lower().count("r")
check_u = conatenated_string.lower().count("u")
check_e = conatenated_string.lower().count("e")
check_l = conatenated_string.lower().count("l")
check_o = conatenated_string.lower().count("o")
check_v = conatenated_string.lower().count("v")
check_e = conatenated_string.lower().count("e")

true_check = check_t + check_r + check_u + check_e
love_check = check_l + check_o + check_v + check_e
final_num = str(true_check) + str(love_check)
converted_num = int(final_num)

if converted_num < 10 or converted_num > 90:
  print(f"Your score is {final_num}, you go together like coke and mentos.")
elif converted_num > 40 and converted_num < 50:
  print(f"Your score is {final_num}, you are alright together.")
else:
  print(f"Your score is {final_num}.")




import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

take_input_from_user = int(input("What do you Choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if take_input_from_user == 0:
    print(rock)
elif take_input_from_user == 1:
    print(paper)
else:
    print(scissors)

random_int_generators = random.randint(0,2)

if random_int_generators == 0:
    print(rock)
elif random_int_generators == 1:
    print(paper)
else:
    print(scissors)

if (take_input_from_user == 0 and random_int_generators == 2) or ( take_input_from_user == 2 and random_int_generators == 1) or (take_input_from_user == 1 and random_int_generators == 0):
    print("You won!")
elif take_input_from_user == random_int_generators:
    print("Its an Draw")
else:
    print("Computer won!")
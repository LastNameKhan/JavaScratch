import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
user_difficulty = input("Choose difficulty level 'easy' or 'hard': ").lower()

easy_chances = 10
hard_chances = 5
number = random.randint(1,101)

def result(chances):
    while not chances == 0:
        user_guess = int(input("Guess the number"))
        if user_guess == number:
            print("Yeah!!, You have won!")
        elif user_guess > number:
            print("Too High!")
            chances -= 1
            print(f"You have {chances} chances left.")
        elif user_guess < number:
            print("Too Low")
            chances -= 1
            print(f"You have {chances} chances left.")
        elif chances == 0:
            print("You have no more attempts Left. Better Luck Next Time!")



if user_difficulty == "hard":
    result(5)
elif user_difficulty == "easy":
    result(10)




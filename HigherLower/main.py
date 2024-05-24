import random
from art import logo
from art import vs

print(logo)
# print(vs)

score = 0

compare_a_questions = {"Does the population of New York City exceed 8 million?":True,
                       "Does Cristiano Ronaldo have more than 200 million Instagram followers?":False,
                       "Is Jeff Bezos' net worth higher than $150 billion?":True,
                       "Does 'The Shawshank Redemption' have an IMDb rating higher than 9.0?":False,
                       "CompareA5":True,
                       "CompareA6":False,"CompareA7":True,"CompareA8":False,"CompareA9":True}
compare_b_questions = {"Does the population of Los Angeles exceed 4 million?":True,
                       "Does Kim Kardashian have more than 200 million Instagram followers?":False,
                       "Is Elon Musk's net worth higher than $150 billion?":True,
                       "Does 'The Godfather' have an IMDb rating higher than 9.0?":False,"CompareB5":True,"CompareB6":False,"CompareB7":True,"CompareB8":False,"CompareB9":True}


continuation = True

while continuation:
    pick_question_a = random.choice(list(compare_a_questions.keys()))
    pick_question_b = random.choice(list(compare_b_questions.keys()))

    print(pick_question_a)
    print(vs)
    print(pick_question_b)
    user_ans = input("Which is correct? Type 'A' or 'B': ").lower()
    if user_ans == "a" and compare_a_questions[pick_question_a] == True:
        score += 1
        print(f"You guessed it correct and your score is {score}")
    elif user_ans == "b" and compare_b_questions[pick_question_b] == True:
        score += 1
        print(f"You guessed it correct and your score is {score}")
    else:
        print("You Lost better luck next time")
        print(f"Your Final Score is :{score}")
        continuation = False


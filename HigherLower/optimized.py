from art import logo
from art import vs
from game_data import data
import random

print(logo)

game_over = False
score = 0


def extract_data():
    """It extracts the individual key and value data from the random selected Dictionary"""
    comparison_question = random.choice(data)
    name = comparison_question["name"]
    description =  comparison_question["description"]
    country = comparison_question["country"]
    print(f"{name}, a {description}, from {country}.")
    followers = comparison_question["follower_count"]
    return followers

def compare():
    global game_over
    global score
    Comapre_A_Followers = extract_data()
    print(Comapre_A_Followers)
    print(vs)
    Comapre_B_Followers = extract_data()
    print(Comapre_B_Followers)
    user_input = input("Who has more followers? Type 'A' or 'B'")
    if user_input == "A" and Comapre_A_Followers > Comapre_B_Followers:
        score += 1
        print(score)
    elif user_input == "B" and Comapre_B_Followers > Comapre_A_Followers:
        score += 1
        print(score)
    else:
        print(f"Sorry That's wrong, Final Score: {score}")
        game_over = True

while not game_over:
    compare()

import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def player_one_card():
    player_one = random.sample(cards,2)
    print(player_one)

def computer_card():
    cpu = random.sample(cards,2)
    print(cpu)


player_one_card()
computer_card()
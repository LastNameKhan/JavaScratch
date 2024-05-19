import random

# First give player one two cards and sum them up then repeat same with player two
# Now ask player_one for another card

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

total_player_one = 0
player_one = []
def player_one_card():
    player_one = random.sample(cards,2)
    total_player_one = sum(player_one)
    print(total_player_one)
    if total_player_one < 21:
        another_card = input("Would you like to get another card 'y' or 'n' ?").lower()
        if another_card == "y":
            random.sample(cards,1).append(player_one)
            print(player_one)
    # print(player_one)
   

total_cpu = 0
cpu = []
def computer_card():
    cpu = random.sample(cards,2)
    total_cpu = sum(cpu)
    if total_cpu < 21:
        random.sample(cards,1).append(player_one)
        print(player_one)
    print(cpu)
    print(total_cpu)

player_one_card()
computer_card()
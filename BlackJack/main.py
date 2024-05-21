import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the Deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

print(user_cards)
print(computer_cards)








# game_start = input("Are you ready to start the Game Type 'y' or 'n': ").lower()

# if game_start == 'y':
#     player_one_card = random.sample(cards,2)
#     player_one_total = sum(player_one_card)
#     cpu_card = random.sample(cards,2)
#     cpu_total = sum(cpu_card)
#     print(player_one_card)
#     print(player_one_total)
#     if player_one_total == 21:
#         print(f"You Win cpu:{cpu_total} you:{player_one_total}")
#     elif cpu_total == 21:
#         print(f"Cpu Wins cpu:{cpu_total} you:{player_one_total}")
#     elif player_one_total == cpu_total:
#         print(f"Snap!! It's an Draw cpu:{cpu_total} you:{player_one_total}")
#     elif player_one_total < 21:
#         plus_one_input = input("Would you like to take another Hit!!!? 'y' or 'n': ").lower()
#         if plus_one_input == 'y':
#             plus_one = random.sample(cards,1)
#             player_one_card.extend(plus_one)
#             plus_one_total = sum(player_one_card)
#             print(player_one_card)
#             print(plus_one_total)
#             print(cpu_card)
#             print(cpu_total)
#             if plus_one_total < cpu_total and cpu_total <= 21:
#                 print(f"Cpu Wins cpu:{cpu_total} you:{plus_one_total}")
#             elif plus_one_total > cpu_total and plus_one_total <= 21:
#                 print(f"You Win cpu:{cpu_total} you:{plus_one_total}")
#             elif plus_one_total and cpu_total > 21:
#                 print(f"No Winner cpu:{cpu_total} you:{plus_one_total}")
#         else:
#             if player_one_total < cpu_total and cpu_total < 21:
#                 print(f"Cpu Wins cpu:{cpu_total} you:{player_one_total}")
#             elif player_one_total > cpu_total and player_one_total < 21:
#                 print(f"You Win cpu:{cpu_total} you:{player_one_total}")


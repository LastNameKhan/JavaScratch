import random
# Step1 - Pick and random word

word_list = [
    "elephant", "banana", "guitar", "sunshine", "laptop", "mountain", "chocolate", "umbrella", "telescope", "kangaroo",
    "computer", "pineapple", "keyboard", "rainbow", "backpack", "dictionary", "helicopter", "sandwich", "watermelon", "bicycle",
    "telephone", "calendar", "fireplace", "spaceship", "strawberry", "suitcase", "microphone", "volcano", "pinecone", "scissors",
    "caterpillar", "skyscraper", "hamburger", "flashlight", "dragonfly", "skateboard", "whale", "cucumber", "binoculars", "balloon",
    "carousel", "basketball", "firework", "mosquito", "snowflake", "penguin", "giraffe", "zucchini", "snorkel", "sunglasses",
    "accordion", "waterfall", "crocodile", "football", "butterfly", "toothbrush", "candle", "paintbrush", "honeycomb", "shoelaces",
    "seahorse", "compass", "puzzle", "dragon", "piano", "crayon", "toucan", "drumstick", "mushroom", "stethoscope", "whisk", 
    "parachute", "strainer", "beehive", "spider", "platypus", "firecracker", "flamingo", "squirrel", "koala", "trampoline",
    "peacock", "jellyfish", "cornucopia", "spacesuit", "coconut", "rattlesnake", "toothpaste", "bobsled", "snowman", "grapefruit",
    "windmill", "bowtie", "seashell", "caterpillar", "lightbulb", "mosquito", "dolphin", "dandelion", "earmuffs", "raincoat"
]


choosen_one = random.choice(word_list)
length_of_choosen_one = len(choosen_one)

empty_blanks = []
for blanks in range(0,length_of_choosen_one):
    empty_blanks.append("_")
print(empty_blanks)
print(choosen_one,length_of_choosen_one)

end_of_game = False
while not end_of_game:
    user_input_check = input("Guess the Character? \n").lower()
    
    for position in range(len(choosen_one)):
        char_guess = choosen_one[position]
        if char_guess == user_input_check:
            empty_blanks[position] = char_guess
    
    print(empty_blanks)

    if "_" not in empty_blanks:
        end_of_game = True
        print("You win!!!!!")
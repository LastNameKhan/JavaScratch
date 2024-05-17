import art


print(art.logo)

bid_finish = False

participants_data = {}
while not bid_finish:
    participants_name = input("What is your name?: ")
    participants_bid = int(input("What's your bid?: $"))
    participants_data[participants_name] = participants_bid
    participants_ans = input("Are there any other bidders? Type 'Yes' or 'No'. ").lower()
    if participants_ans == "no":
        bid_finish = True
        winner_amount = 0
        winner_name = ""
        for key in participants_data:
            if participants_data[key] > winner_amount:
                winner_amount = participants_data[key]
                winner_name = key
                print(f"The winner is {winner_name} with a bid of ${winner_amount}")
    elif participants_ans == "yes":
        
            
        

       
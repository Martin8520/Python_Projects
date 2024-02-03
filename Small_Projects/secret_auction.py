from Small_Projects.secret_auction_art import logo

print(logo)
bid_list = {}
run = True
while run is True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    bid_list[name] = bid
    print(bid_list)


    def highest_bid(bidding_record):
        h_bid = 0
        winner = ""
        for bidder in bidding_record:
            bid_amount = bidding_record[bidder]
            if bid_amount > h_bid:
                h_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${h_bid}")


    restart = input("Are there any other bidders? Type 'yes' or 'no'. ")
    if restart == "yes":
        run = True
        print("\n" * 100)
    elif restart == "no":
        highest_bid(bid_list)
        run = False
    else:
        print("Invalid input")

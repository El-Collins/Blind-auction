from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo

print(logo)

print("Welcome to the secret auction program.")

isbidders = True

bids = {}


def auction(bidding_record):

    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while isbidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid? $ "))
    bids[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ")

    if other_bidders == "no":
        isbidders = False
        auction(bids)
    elif other_bidders == "yes":
        clear()

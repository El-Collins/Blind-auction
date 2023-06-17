from replit import clear
#HINT: You can call clear() to clear the output in the console.

from art import logo


should_contine = False

bids = {}

def highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = highest_bid
    print(f"The winner is {winner} with a bid of ${highest_bid}")


while not should_contine:
  print(logo)
  name = input("What is your name? \n")
  bid = int(input("What's your bid? $ \n"))
  bids[name] = bid
  other_bidder = input("Are they any other bidders? Type 'yes' or 'no' \n")


  if other_bidder == "no":      
    should_contine = True
    highest_bidder(bids)
    
  elif other_bidder == "yes":
    clear()

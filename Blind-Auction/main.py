from replit import clear
import art
bidders = {}

def calculate_highest_bid(biddernames):
  final_value = 0
  winner = ""
  for bids in biddernames:
    bid_value = biddernames[bids]
    if bid_value > final_value:
      final_value = bid_value
      winner = bids
  print(f"The winning bidder is {winner} with a bid of ${final_value}.")

bidding = True
while bidding == True:
  print(art.logo)
  name = input("What is your name?\n")
  bids = int(input("Place your bid:\n$"))
  bidders[name] = bids
  should_continue = input("Are there other bidders? Yes or No:\n").lower()
  if should_continue == "yes":
    clear()
  else:
    should_continue == "no"
    clear()
    calculate_highest_bid(bidders)
    bidding = False





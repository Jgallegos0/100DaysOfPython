import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def dealer_sum(thelist):
  dealer_total = 0
  for num in thelist:
    dealer_total += num
  return dealer_total

def your_sum(thelist):
  your_total = 0
  for num in thelist:
    your_total += num
  return your_total

def jack_black():
  dealer_deck = []
  your_deck = []
  #DEALER DECK
  dealer_deck.append(cards[random.randint(0,12)])
  dealer_deck.append(cards[random.randint(0,12)])
  #YOUR DECK
  your_deck.append(cards[random.randint(0,12)])
  your_deck.append(cards[random.randint(0,12)])
  #SUM
  dealertotal = dealer_sum(dealer_deck)
  yourtotal = your_sum(your_deck)

  print(dealer_deck)
  print(f"Dealers first card is {dealer_deck[0]}")
  print(f"Dealers total is: {dealertotal}")
  
  print(your_deck)
  print(f"Your first card is: {your_deck[0]}")
  print(f"Your total is: {yourtotal}")

  next_card = input("Add another card? y or n: ")
  if next_card == "y":
    #ADD NEW CARD TO EACH DECK
    dealer_deck.append(cards[random.randint(0,12)])
    your_deck.append(cards[random.randint(0,12)])
    #NEW TOTAL
    dealertotal = dealer_sum(dealer_deck)
    yourtotal = your_sum(your_deck)
    #DISPLAY
    print(dealer_deck)
    print(f"Dealers first card is {dealer_deck[0]}")
    print(f"Dealers total is: {dealertotal}")
  
    print(your_deck)
    print(f"Your first card is: {your_deck[0]}")
    print(f"Your total is: {yourtotal}")

  else:
    if yourtotal > dealertotal:
      print(f"Your total is {yourtotal}, dealer's total is {dealertotal} you win")
    else:
      print(f"Dealer total is {dealertotal}, yours is {yourtotal} you lose")
    #SHOW WHO WON
#--------------------

#START
#print(art.logo)
decision = input("Do you want to play black jack? y or n: ")
#DECISION
if decision == "y":
  #DRAW CARDS
  jack_black()
else:
  continue_game = False
############### Our Blackjack House Rules #####################

#In Progress

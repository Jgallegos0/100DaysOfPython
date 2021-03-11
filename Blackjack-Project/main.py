import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def sum(card1, card2):
  value = card1 + card2
  return value
#DEALER DECK
dealer_deck = []
dealer_deck.append(cards[random.randint(0,12)])
dealer_deck.append(cards[random.randint(0,12)])
print(dealer_deck)

one = dealer_deck[0]
two = dealer_deck[1]
total = sum(one, two)
print(total)

#YOUR DECK
your_deck = []
your_deck.append(cards[random.randint(0,12)])
your_deck.append(cards[random.randint(0,12)])
print(your_deck)

one = your_deck[0]
two = your_deck[1]
total = sum(one, two)
print(total)
############### Our Blackjack House Rules #####################

#In Progress

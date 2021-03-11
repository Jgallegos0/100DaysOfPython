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

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


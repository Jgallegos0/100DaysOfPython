import random
from art import logo
from replit import clear

def deal_card():
  """Returns random card from deck"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card
def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  return sum(cards)
def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw 😌"
  elif computer_score == 0:
    return "Lose, opponent has a Blackjack 😣"
  elif user_score == 0:
    return "Win with a blackjack 🙂"
  elif user_score > 21:
    return "Went over, you lose 😣"
  elif computer_score > 21:
    return "Opponent went over, you win 🙂"
  elif user_score > computer_score:
    return "You win 🙂"
  else:
    return "You lose"

def play_game():
  user_cards = []
  computer_cards = []


  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"Your cards: {user_cards}, Current score: {user_score}")
    print(f"Dealers first card: {computer_cards[0]}")

    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      should_deal = input("Get another card? y or n:\n")
      if should_deal == 'y':
        user_cards.append(deal_card())       
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  print(f"Your final hands: {user_cards}, your final score: {user_score}.")
  print(f"Dealer's final hands: {computer_cards}, Dealer's final score {computer_score}")
  print(compare(user_score, computer_score))

print(logo)
while input("Do you want to play Black Jack? 'y' or  'n':\n") == 'y':
  clear()
  play_game()


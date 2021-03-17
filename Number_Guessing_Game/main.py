import random
from art import logo
from replit import clear

def choice():
  numbers = [1,2,3,4,5,6,7,8,9,10]
  number = random.choice(numbers)
  return number

def easy(difficulty): #10tries
  tries = 10
  number = choice()
  while tries != 0:
    guess = int(input("Guess a number: "))
    if guess == number:
      tries = 0
      print("Correct!")
    elif guess > number:
      tries -= 1
      print("Too high")
      print(f"You have {tries} tries left")
    elif guess < number:
      tries -= 1
      print("Too low")
      print(f"You have {tries} tries left")
  print(f"Correct answer was: {number}")

def hard(difficulty): #5tries
  tries = 5
  number = choice()
  while tries != 0:
    guess = int(input("Guess a number: "))
    if guess == number:
      tries = 0
      print("Correct!")
    elif guess > number:
      tries -= 1
      print("Too high")
      print(f"You have {tries} tries left")
    elif guess < number:
      tries -= 1
      print("Too low")
      print(f"You have {tries} tries left")
  print(f"Correct answer was: {number}")
  
#Function to determine difficulty
def determine(difficulty):
  if difficulty == 'easy':
    easy(difficulty)
  else:
    difficulty == 'hard'
    hard(difficulty)
    
#Game begins
start_game = True
while start_game:
  print(logo)
  print("I'm thinking of a number between 1 and 100")
  level = input("Choose difficulty: 'easy' or 'hard'\n")
  determine(level)
  go_again = input("Do you want to play again? 'y' or 'n':\n")
  if go_again == 'y':
    clear()
    start_game = True
  else:
    go_again == 'n'
    start_game = False







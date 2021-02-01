import random
import hangman
import words
from replit import clear
#RANDOM WORD GENERATOR
wordchoice = random.choice(words.word_list)
#LENGTH OF THE WORD
length_of_word = len(wordchoice)
#TOTAL LIVES THE USER HAS
lives = 6
#WELCOME MESSAGE
print(hangman.logo)
#CREATE A DISPLAY LIST FOR THE CHOSEN WORD
display = []
for letter in wordchoice:
  display += "_"
#CONTROL VARIABLE
end_of_game = False
#GAME BEGINS/LOOP
while not end_of_game:
  #ASK USER TO GUESS A LETTER
  guess = input("Guess a letter:\n").lower()
  
  #CLEAR PREVIOUS ANSWERS TO IMPROVE UI
  clear()
  #IF USER REPEATS GUESS
  if guess in display:
    print("You already chose that word, try again.")

  #CHECK IF THE LETTER IS IN THE WORD
  for position in range(length_of_word):
    letter = wordchoice[position]
    if guess == letter:
      display[position] = letter
  print(f"{' '.join(display)}")
  #print(hangman.stages[lives])

  #IF THE LETTER IS NOT IN THE WORD
  if guess not in wordchoice:
    lives -= 1
    print("That letter is not in the word, you lose a life.")
    #print(hangman.stages[lives])
  #IF THE USER HAS GUESSED THE WORD
  if "_" not in display:
    end_of_game = True
    print("Game over, you won.")
  #IF THE USER HAS LOST ALL LIVES
  if lives == 0:
    end_of_game = True
    print("Game over")
  #PRINT CURRENT STAGE
  print(hangman.stages[lives])
  #HINT, HINT MAY GIVE USER A WORD THAT WAS ALREADY USED
  if lives == 3:
    lives -= 1
    hint = input("Do you want one hint? Y or N?\n").lower()
    if hint == "y":
      clue = random.randint(0, length_of_word - 1)
      if wordchoice[clue] not in display:
        print(f"Your hint is: {wordchoice[clue]}.")
      else:
       clue = random.randint(0, length_of_word - 1)
       print(f"Your hint is: {wordchoice[clue]}.") 
#REVEAL THE WORD  
if end_of_game == True:
  if "_" in display:
    print(f"The word was: {wordchoice}.")

  






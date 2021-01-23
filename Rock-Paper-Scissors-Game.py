import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
answer = input("Welcome! Rock, Paper, or Scissors?\n")
answer_lower = answer.lower()
signs = [rock, paper, scissors]

choose = random.choice(signs)

if answer_lower == "rock":
  print(f"{rock}\n{choose}")
  if choose == signs[0]:
   print("Its a tie!")
  elif choose == signs[1]:
   print("You lose")
  else:
    choose == signs[2]
    print("You win!")
elif answer_lower == "paper":
  print(f"{paper}\n{choose}")
  if choose == signs[0]:
   print("You win!")
  elif choose == signs[1]:
   print("It's a tie!")
  else:
    choose == signs[2]
    print("You lose!")
else:
  answer_lower == "scissors"
  print(f"{scissors}\n{choose}")
  if choose == signs[0]:
   print("You lose!")
  elif choose == signs[1]:
   print("You win!")
  else:
    choose == signs[2]
    print("It's a tie!")
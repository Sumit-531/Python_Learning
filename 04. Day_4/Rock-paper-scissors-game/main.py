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

#Write your code below this line 👇

choice_of_user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice_of_user == 0:
  print(rock)
elif choice_of_user == 1:
  print(paper)
elif choice_of_user == 2:
  print(scissors)
else:
  print("Wrong choice!")

print("Computer chose: ")
computer_chose = random.randint(0,2)


if computer_chose == 0:
  print(rock)
if computer_chose == 1:
  print(paper)
if computer_chose == 2:
  print(scissors)

#Decision

#Draw Rules
if choice_of_user == 0 and computer_chose == 0:
  print("Draw.")
if choice_of_user == 1 and computer_chose == 1:
  print("Draw.")
if choice_of_user == 2 and computer_chose == 2:
  print("Draw.")

#Rock:
if choice_of_user == 0 and computer_chose == 2:
  print("You win")
if choice_of_user == 2 and computer_chose == 0:
  print("You loose")

#Scissors:
if choice_of_user == 2 and computer_chose == 1:
  print("You win")
if choice_of_user == 1 and computer_chose == 2:
  print("You loose")

#Papers
if choice_of_user == 1 and computer_chose == 0:
  print("You win")
if choice_of_user == 0 and computer_chose == 1:
  print("You loose")

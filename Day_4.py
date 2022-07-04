# EXERCISE #1 - Heads or Tails
# You are going to write a virtual coin toss program. It will randomly tell
# the user "Heads" or "Tails".

import random

heads_tails = random.randint(1, 100)
if heads_tails % 2 == 0:
    print('Heads')
else:
    print('Tails')

#------------------------------------------------------------------------------#

#EXERCISE #2 - Who's Paying
# You are going to write a program which will select a random name from a list
# of names. The person selected will have to pay for everybody's food bill.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

random_name = random.randint(0, len(names) - 1)
print(names[random_name])

#------------------------------------------------------------------------------#

# EXERCISE #3 - Treasure Map
# You are going to write a program which will mark a spot with an X.
# Your job is to write a program that allows you to mark a square on the map
# using a two-digit system. The first digit is the vertical column number and
# the second digit is the horizontal row number.

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

first_num = int(position[0])
second_num = int(position[1])

map[second_num - 1][first_num - 1] = 'X'

print(f"{row1}\n{row2}\n{row3}")

#------------------------------------------------------------------------------#

# EXERCISE #4 - Rock Paper Scissors

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

print('Welcome to a friendly game of Rock Paper Scissors.')

human = int(input("""What do you choose? Type "1" for Rock, "2" for Paper, or "3"
for Scissors.\n"""))
computer = random.randint(0, 2)

options = [rock, paper, scissors]
human_choice = options[human - 1]
computer_choice = options[computer]

print("You chose:")
print(human_choice)
print("Computer chose:")
print(computer_choice)

if human_choice == options[0] and computer_choice == options[1]:
    print('Sorry, you lose :(')
elif human_choice == options[1] and computer_choice == options[2]:
    print('You Win :)')
elif human_choice == options[2] and computer_choice == options[0]:
    print('Sorry, you lose :(')
elif computer_choice == options[0] and human_choice == options[1]:
    print('You Win :)')
elif computer_choice == options[1] and human_choice == options[2]:
    print('Sorry, you lose :(')
elif computer_choice == options[2] and human_choice == options[0]:
    print('You Win :)')
else:
    print("It's a draw!")

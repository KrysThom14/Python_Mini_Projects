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

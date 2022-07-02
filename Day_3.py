# EXERCISE #1 - Odd or Even
# Write a program that works out whether if a given number is an odd or
# even number.

number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print('This is an even number.')
else:
    print('This is an odd number.')

#------------------------------------------------------------------------------#

# EXERCISE #2 - BMI Calculator 2.0
# Write a program that interprets the Body Mass Index (BMI) based on a user's
# weight and height. It should tell them the interpretation of their BMI based
# on the BMI value.

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = float(weight) / float(height)**2
bmi_rounded = round(bmi, 1)

if bmi <= 18.5:
    value = 'underweight'
elif bmi > 18.5 and bmi <= 25:
    value = 'normal weight'
elif bmi > 25 and bmi <= 30:
    value = 'slightly overweight'
elif bmi > 30 and bmi <= 35:
    value = 'obese'
else:
    value = 'clinically obese'

print(f'Your BMI is {bmi_rounded}, you are {value}.')

#------------------------------------------------------------------------------#

# EXERCISE #3
# Write a program that works out whether if a given year is a leap year. A
# normal year has 365 days, leap years have 366, with an extra day in February.
# How to know if it is a leap year:
# 1. on every year that is divisible by 4
# 2. except every year that is evevly divisible by 100
# 3. unless the year is also evenly divisible by 400

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 != 0:
        if year % 400 != 0:
            print(f'{year} is A Leap Year.')
        else:
            print(f'{year} is Not A Leap Year.')
    else:
        print(f'{year} is Not A Leap Year.')
else:
    print(f'{year} is Not A Leap Year.')

#------------------------------------------------------------------------------#

# EXERCISE #4 - Pizza Order
# Congratulations, you've got a job at Python Pizza. Your first job is to build
# an automatic pizza order program. Based on a user's order, work out their
# final bill.
# Small Pizza: $15; Medium Pizza: $20; Large Pizza: $25
# Pepperoni for Small Pizza: +$2; Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: +$1

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == 'S':
    bill += 15
elif size == 'M':
    bill += 20
else:
    bill += 25

if add_pepperoni == 'Y':
    if size == 'S':
        bill += 2
    else:
        bill += 3

if extra_cheese == 'Y':
    bill += 1

print(f'Your final bill is: ${bill}')

#------------------------------------------------------------------------------#

# EXERCISE #5 - Love Calculator
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
# Take both people's names and check for the number of times the letters in the
# word TRUE occurs. Then check for the number of times the letters in the word
# LOVE occurs. Then combine these numbers to make a 2 digit number.

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1_lower = name1.lower()
name2_lower = name2.lower()

true1 = name1_lower.count('t') + name2_lower.count('t')
true2 = name1_lower.count('r') + name2_lower.count('r')
true3 = name1_lower.count('u') + name2_lower.count('u')
true4 = name1_lower.count('e') + name2_lower.count('e')

love1 = name1_lower.count('l') + name2_lower.count('l')
love2 = name1_lower.count('o') + name2_lower.count('o')
love3 = name1_lower.count('v') + name2_lower.count('v')
love4 = name1_lower.count('e') + name2_lower.count('e')

true_score = true1 + true2 + true3 + true4
love_score = love1 + love2 + love3 + love4
total_score = str(true_score) + str(love_score)

if int(total_score) < 10 or int(total_score) > 90:
    print(f'Your score is {total_score}, you go together like coke and mentos.')
elif int(total_score) > 40 and int(total_score) < 50:
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}.')

#------------------------------------------------------------------------------#

# EXERCISE #6 - Treasure Island
# Make your own "Choose Your Own Adventure" game. Use conditionals such as if,
# else, and elif statements to lay out the logic and the story's path in your
# program.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input("""You're at a crossroad. Where do you want to go? Type
"left" or "right". \n""").lower()

if choice_1 == 'left':
    choice_2 = input("""You've come to a lake. There is an island in the
middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim
across. \n""").lower()

    if choice_2 == 'wait':
        choice_3 = input("""You arrive at the island unharmed. There is a house
with 3 doors. One red, one yellow, and one blue. Which color do you
choose? \n""").lower()

        if choice_3 == 'yellow':
            print("You found the treasure! You Win!")
        elif choice_3 == 'blue':
            print("""You enter a room with a giant hole. You fall in and die.
Game Over!""")
        else:
            print("It's a room full of fire! Game Over!")

    else:
        print("You are eaten by a gian sea monster. Game Over!")
else:
    print("You run into a bear and it kills you. Game Over!")

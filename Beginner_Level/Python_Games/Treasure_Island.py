# This is a super simple choose your own "Choose Your Own Adventure" game. I
# used conditionals such as if, else, and elif statements to lay out the logic
# and the story's path in the program.

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

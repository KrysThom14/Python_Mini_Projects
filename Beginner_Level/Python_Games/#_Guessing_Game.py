import random

logo = """
  _____                   ________         _  __           __
 / ___/_ _____ ___ ___   /_  __/ /  ___   / |/ /_ ____ _  / /  ___ ____
/ (_ / // / -_|_-<(_-<    / / / _ \/ -_) /    / // /  ' \/ _ \/ -_) __/
\___/\_,_/\__/___/___/   /_/ /_//_/\__/ /_/|_/\_,_/_/_/_/_.__/\__/_/

"""

correct_number = random.randint(1,100)

def easy_mode():
    turns = 10
    print(f"You have 10 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while guess != correct_number:
        turns -= 1
        if turns == 0:
            print("You've run out of guesses. GAME OVER.")
            break
        elif guess < correct_number:
            print("Too low. Try again.")
            print(f"You have '{turns}' attempts left.\n")
        elif guess > correct_number:
            print("Too high. Try again.")
            print(f"You have '{turns}' attempts left.\n")
        guess = int(input("Next guess: "))
    if guess == correct_number:
        print(f"You got it! The answer was {correct_number}.")

def hard_mode():
    turns = 5
    print(f"You have 5 attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    while guess != correct_number:
        turns -= 1
        if turns == 0:
            print("You've run out of guesses. GAME OVER.")
            break
        elif guess < correct_number:
            print("Too low. Try again.")
            print(f"You have '{turns}' attempts left.\n")
        elif guess > correct_number:
            print("Too high. Try again.")
            print(f"You have '{turns}' attempts left.\n")
        guess = int(input("Next guess: "))
    if guess == correct_number:
        print(f"You got it! The answer was {correct_number}.")

print(logo)
print("Welcome to the Number Guessing Game!")
difficulty_level = (input("""Choose a difficulty. Type 'easy' for 10 attempts
or 'hard' for 5 attempts: """)).lower()
print("")
print("I'm thinking of a number between 1 and 100.")

def play_game(difficulty_level):
    if difficulty_level == 'easy':
        easy_mode()
    elif difficulty_level == 'hard':
        hard_mode()

play_game(difficulty_level)

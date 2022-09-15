from Higher_or_Lower_Game_Data import data
import random

logo = """
   __ ___      __                        __
  / // (_)__ _/ /  ___ ____  ___  ____  / /  ___ _    _____ ____
 / _  / / _ `/ _ \/ -_) __/ / _ \/ __/ / /__/ _ \ |/|/ / -_) __/
/_//_/_/\_, /_//_/\__/_/    \___/_/   /____/\___/__,__/\__/_/
       /___/
"""

vs = """
  _   __
 | | / /__
 | |/ (_-<_
 |___/___(_)
"""

playing_game = True
score = 0

person_a = data[random.randint(0, len(data)-1)]
person_b = data[random.randint(0, len(data)-1)]

while playing_game:

    if score > 0:
        person_a = person_b
        person_b = data[random.randint(0, len(data)-1)]

    if person_a == person_b:
        person_b = data[random.randint(0, len(data))]

    person_a_client_side = f"{person_a['name']}: a {person_a['description']}, from {person_a['country']}"
    person_b_client_side = f"{person_b['name']}: a {person_b['description']}, from {person_b['country']}"

    print(logo)

    if score > 0:
        print(f"Correct! Current Score: {score}")

    print(f'Person A = {person_a_client_side}.')

    print(vs)

    print(f'Person B = {person_b_client_side}.\n')

    user_guess = input("Who has more Instagram folowers? Type 'A' or 'B': ").lower()

    if user_guess == 'a':
        if person_a['follower_count'] > person_b['follower_count']:
            score += 1
        else:
            playing_game = False
    if user_guess == 'b':
        if person_b['follower_count'] > person_a['follower_count']:
            score += 1
        else:
            playing_game = False

    print("")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("")
print(f"Sorry, incorrect. Final Score: {score}")

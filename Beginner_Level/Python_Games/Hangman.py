import random
from hangman_word_options import word_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

chosen_word = random.choice(word_list)

lives = 6

display = []
for i in range(len(chosen_word)):
    display.append('_')

playing_game = True

while playing_game:

    print(stages[lives])
    print(f"{' '.join(display)}")

    guess = input('Please guess a letter:\n').lower()

    if guess in display:
        print(f"You've already guessed {guess}. Try again.")

    for i in range(len(chosen_word)):
        spot = chosen_word[i]
        if guess == spot:
            display[i] = spot

    if guess not in chosen_word:
        lives -= 1
        print(f'{guess} is not in the word. Lives left = {lives}')

    if '_' not in display:
        playing_game = False
        print(display)
        print('You Won!')
    elif lives == 0:
        playing_game = False
        print(stages[lives])
        print('You Lose!')

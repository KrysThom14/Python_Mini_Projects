# EXERCISE #1 - Average Height
# You are going to write a program that calculates the average student height
# from a List of heights. The average height can be calculated by adding all the
# heights together and dividing by the total number of heights. You should are
# not allowed to use the sum() or len() functions in your answer.

num_heights = 0
total_heights = 0
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  num_heights += 1
  total_heights += student_heights[n]

average_height = round(total_heights / num_heights)
print(average_height)

#------------------------------------------------------------------------------#

# EXERCISE #2 - Highest Score
# You are going to write a program that calculates the highest score from a List
# of scores. Important you are not allowed to use the max or min functions. The
# output words must match the example. i.e The highest score in the class is: x

x = 0
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
    if student_scores[n] > x:
      x = student_scores[n]

print(f'The highest score in the class is: {x}')

#------------------------------------------------------------------------------#

# EXERCISE #3 - Adding Evens
# You are going to write a program that calculates the sum of all the even
# numbers from 1 to 100. Thus, the first even number would be 2 and the last
# one is 100: (i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100). Important, there should
# only be 1 print statement in your console output. It should just print the
# final total and not every step of the calculation.

x = 0
for n in range(1, 101):
    if n % 2 == 0:
        x += n
print(x)

#------------------------------------------------------------------------------#

# EXERCISE #4 - FizzBuzz
# You are going to write a program that automatically prints the solution to the
# FizzBuzz game. Your program should print each number from 1 to 100 in turn.
# When the number is divisible by 3 then instead of printing the number it
# should print "Fizz". When the number is divisible by 5, then instead of
# printing the number it should print "Buzz". And if the number is divisible by
# both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)

#------------------------------------------------------------------------------#

# EXERCISE #5 - Password Generator
# Create a program that gives the user a complex, randomized sample password
# that they can use based on the parameters that they ask for.

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

random_letters = []
random_symbols = []
random_numbers = []

if nr_letters > 0:
    for letter in range(0, nr_letters):
        random_letters += letters[random.randint(0, 51)]

if nr_symbols > 0:
    for symbol in range(0, nr_symbols):
        random_symbols += symbols[random.randint(0, 8)]

if nr_numbers > 0:
    for num in range(0, nr_numbers):
        random_numbers += numbers[random.randint(0, 9)]

full_password = random_letters + random_symbols + random_numbers
random_password = random.sample(full_password, len(full_password))
full_random_password = ''.join(random_password)
print(full_random_password)

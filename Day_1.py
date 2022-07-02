# EXERCISE #1 - Write a program that switches the values stored in the
# variables a and b.

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

#------------------------------------------------------------------------------#

# EXERCISE #2 - Band Name Generator
# 1. Create a greeting for your program.
# 2. Ask the user for the city that they grew up in.
# 3. Ask the user for the name of a pet.
# 4. Combine the name of their city and pet and show them their band name.
# 5. Make sure the input cursor shows on a new line

print('Welcome to the Band Name Generator!')
city = input('What city did you grow up in?\n')
pet = input('What is the name of one of your pets?\n')
print('Your band name could be ' + city + ' ' + pet + '.')

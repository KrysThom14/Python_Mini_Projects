# EXERCEISE #1 - Write a program that adds the digits in a 2 digit number.
# e.g. if the input was 35, then the output should be 3 + 5 = 8

two_digit_number = input("Type a two digit number: ")

sum_digits = int(two_digit_number[0]) + int(two_digit_number[1])
print(sum_digits)

#------------------------------------------------------------------------------#

# EXERCISE #2 - BMI Calculator
# Write a program that calculates the Body Mass Index (BMI) from a user's
# weight and height. You should convert the result to a whole number.

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height)**2
print(int(bmi))

#------------------------------------------------------------------------------#

# EXERCISE #3 - Your Life in Weeks
# Create a program using maths and f-Strings that tells us how many days,
# weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our
# time left in this format: "You have x days, y weeks, and z months left."
# Where x, y and z are replaced with the actual calculated numbers.

age = input("What is your current age? ")

ninety_days = int(90 * 365)
ninety_weeks = int(90 * 52)
ninety_months = int(90 * 12)

response_days = int(age) * 365
response_weeks = int(age) * 52
response_months = int(age) * 12

answer_days = ninety_days - response_days
answer_weeks = ninety_weeks - response_weeks
answer_months = ninety_months - response_months

print(f"""You have {answer_days} days, {answer_weeks} weeks, and
{answer_months} months left.""")

#------------------------------------------------------------------------------#

# EXERCISE #4 - Tip Calculator
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

print('Welcome to the Tip Calculator!')
total = input('What was the total bill? ')
tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
split = input('How many people are splitting the bill? ')

tip_convert = (int(tip) / 100) + 1
answer = (float(total) / int(split)) * float(tip_convert)
answer_rounded = round(answer, 2)

print(f'Each person should pay: ${answer_rounded}')

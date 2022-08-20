print('Welcome to the Tip Calculator!')
total = input('What was the total bill? ')
tip = input('What percentage tip would you like to give? 10, 12, or 15? ')
split = input('How many people are splitting the bill? ')

tip_convert = (int(tip) / 100) + 1
answer = (float(total) / int(split)) * float(tip_convert)
answer_rounded = round(answer, 2)

print(f'Each person should pay: ${answer_rounded}')

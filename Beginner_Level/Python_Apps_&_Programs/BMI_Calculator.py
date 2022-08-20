# This is a program that interprets the Body Mass Index (BMI) based on a user's
# weight and height. It tells them the interpretation of their BMI based on
# the BMI value.

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

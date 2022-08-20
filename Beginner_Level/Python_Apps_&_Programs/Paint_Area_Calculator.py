# You are painting a wall. The instructions on the paint can says that
# "1 can of paint can cover 5 square meters" of wall. Given a random height
# and width of wall, calculate how many cans of paint you'll need to buy. This
# program will be forced to round up, since you can't buy '0.3' cans of paint.

number of cans = (wall height * wall width) ÷ coverage per can

import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5 # This number can be changed depending on the paint can instructions

def paint_calc(height, width, cover):
    num_cans = (height * width) / cover
    round_cans = math.ceil(num_cans)
    print(f'You will need {round_cans} cans of paint.')

paint_calc(height=test_h, width=test_w, cover=coverage)

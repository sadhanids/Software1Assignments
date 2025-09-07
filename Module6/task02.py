import random

def dice_rolling(no_of_sides):
    return random.randint(1, no_of_sides)

no_of_sides = int(input('How many sides do you have?: '))

result = 0

while result != no_of_sides:
    result = dice_rolling(no_of_sides)
    print(f"The dice rolling result is: {result}")



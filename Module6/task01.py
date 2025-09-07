import random

def dice_rolling():
    return random.randint(1,6)

result = 0

while result != 6:
    result = dice_rolling()

    print(f'The dice rolling result is: {result}')



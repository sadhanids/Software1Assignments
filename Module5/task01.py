import random
dice = int(input("how many dice to roll?: "))
total = 0
for i in range(dice):
    dice_roll = random.randint(1,6)
    total = i + 1
    print("sum of the numbers is: ", sum(range(i+1)))


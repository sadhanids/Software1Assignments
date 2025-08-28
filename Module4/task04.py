import random

number_given_computer = random.randint(1,10)
number_guess = int(input("Guess a number between 1 to 10: "))
while True :
    if number_guess > number_given_computer:
        print("Too high")
    elif number_guess < number_given_computer:
        print("Too low")
    else:
        print("correct")
        break
    number_guess = int(input("Guess a number between 1 to 10: "))
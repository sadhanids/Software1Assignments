
number =input("Enter a number or type 'done' to quite: ")
numbers =[]
while True:
    if number !="done":
        numbers.append(number)
        number =input("Enter a number or type 'done' to quite: ")
    elif number == "done":
        break
if numbers:
    smallest_number = min(numbers)
    largest_number = max(numbers)

    print(f"The smallest number is: {smallest_number} and the largest number is: {largest_number}")

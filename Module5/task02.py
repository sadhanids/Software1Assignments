numbers = []

while True:
    user_input = input("Enter a number ( or press Enter to quite): ")
    if user_input == "":
        break
    number = float(user_input)
    numbers.append(number)

numbers.sort(reverse=True)
top_five = numbers[:5]

print("Top Five Greatest Numbers in Decending Order: ")
for number in top_five:
    print(number)

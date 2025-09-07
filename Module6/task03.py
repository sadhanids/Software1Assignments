
def conversion (gallons):
    return gallons * 3.78541

while True:
    quantity_of_gasoline = float(input("Enter the quantity of gallons: "))
    if quantity_of_gasoline < 0:
            print("You have entered a negative number. Try again.")
            break
    else:
        liters = conversion (quantity_of_gasoline)
        print(f"{quantity_of_gasoline} of gallons equals to {liters:.2f} liters. ")




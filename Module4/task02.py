conversion_factor = 2.54

number = float(input("Enter number in inches: "))

while number>0 :
    centimeters = number * conversion_factor
    print(f" {number} inches is equal to {centimeters} centimeters")
    number = float(input("Enter number in inches: "))

else:
    print("Program End")
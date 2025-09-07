import math

def pizza_unit_price (diameter_cm, price):
    diameter_m = diameter_cm / 100
    radius = diameter_m/2
    area = math.pi * radius ** 2
    unit_price = price / area
    return unit_price

diameter = float(input("Enter the diameter in cm: "))
price = float(input("Enter the price of pizza in euros: "))

unit_price = pizza_unit_price(diameter, price)
print(f"The unit price of a pizza is {unit_price: .2f} per square meter")
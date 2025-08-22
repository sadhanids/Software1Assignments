

Talent = float(input("Enter Talent: "))

Pounds = float(input("Enter Pounds: "))

Lots = float(input("Enter Lots: "))

Total_grams_from_lots = (Lots*13.3)
Total_grams_from_Pounds = (Pounds*32*13.3)
Total_grams_from_talent = (Talent*20*32*13.3)

Total_grams = Total_grams_from_lots + Total_grams_from_Pounds + Total_grams_from_talent
Kilograms = int(Total_grams/1000)
remainder = Total_grams - Kilograms*1000

The_weight_in_modern_units = Kilograms + remainder
print(f"The weight in modern units is: {Kilograms} kilograms and {remainder:.2f} grams")

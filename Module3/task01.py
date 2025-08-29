length_of_zander = int(input("Enter the length of zander in centimeters: "))
standard_length_of_zander = 42
deviation = standard_length_of_zander - length_of_zander
if length_of_zander < 42:
    print(f"Release the fish back into the lake, {deviation}cm below the standard size of zander ")
else:
    print("The fish meets the legal size of zander, you can keep the fish!")



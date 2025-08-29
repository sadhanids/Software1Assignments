
gender = input("Enter your gender (Male/Female): ").lower()
hemoglobin_value = float(input("Enter hemoglobin value: "))


if gender == "male":
    if hemoglobin_value > 167:
        print("your hemoglobin level is high")
    elif hemoglobin_value < 134:
        print("your hemoglobin level is low")
    else:
        print("your hemoglobin level is normal")

if gender == "female":
    if hemoglobin_value > 155:
        print("your hemoglobin level is high")
    elif hemoglobin_value < 134:
        print("your hemoglobin level is low")
    else:
        print("your hemoglobin level is normal")

else:
    print("Invalid user input, please enter your gender (Male/Female) ")

names = set ()

while True:
    name = input("Enter a name or leave blank to quit: ")
    if name == "":
        break
    if name in names:
        print("Existing Name")

    else:
        print("New Name")
        names.add(name)

    print("\nList of entered names:")
    for n in names:
        print(n)




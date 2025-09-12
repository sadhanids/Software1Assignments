airport_description = {"OTHH" : "Hamad International Airport",
                       "VCBI" : "Bandaranaike International (Colombo)",
                        "WSSS" : "Singapore Changi Airport",
                         "YSSY" : "Sydney Kingsford Smith",
                         "OMDB" : "Dubai International Airport (UAE)",
                       "RJTT" : "Tokyo Haneda Airport (Japan)",
                       "EGLL" : "Heathrow Airport (UK)",
                       "VIDP" : "Indira Gandhi Intl, Delhi (India)",
                       "LFPG" : "Charles de Gaulle, Paris (France)",
                       "CYYZ" : "Toronto Pearson Intl (Canada)"}

while True:
    print("\nChoose an option::")
    print("1 - Enter a new airport")
    print("2 - Fetch airport information")
    print("3 - Exit the program")
    choice = input("Enter your choice:")
    if choice == "1":
        icao = input("Enter ICAO code:").upper()
        name = input("Enter Airport Name: ")
        print(f"Airport {name} with ICAO CODE code {icao} is added.")

    elif choice == "2":
        icao = input("Enter ICAO code to fetch information: ")
        if icao in airport_description:
            print(f"The Airport Name is: {airport_description[icao]}")
        else:
            print("The Airport Name is: Not a valid ICAO code.")

    elif choice == "3":
        print("Exiting the program")
        break

    else:
        print("Invalid input.")

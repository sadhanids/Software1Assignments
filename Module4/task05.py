username = "python"
password = "rules"

no_of_attempts = 5
current_attempt = 1
user_username = input("Enter your username: ")
user_password = input("Enter your password: ")

while True:
    if username == user_username and password == user_password:
        print("welcome")
        break
    else:
        print("wrong username or password")
        user_username = input("Enter your username: ")
        user_password = input("Enter your password: ")
        current_attempt += 1
    if current_attempt == no_of_attempts:
        print("Access Denied")
        break


        







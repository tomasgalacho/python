print("Welcome to Startin Dev Web Campus!\n\nPlease sign up\n")

username1 = input("Enter your dumb username: ")
email1 = input("Enter your childish email: ")
password1 = input("Enter your easy hackable password: ")

print("\nSuccessfully registration\nNow please login for God´s sake\n")

usernameOrEmail = input("Please enter your username or email: ")
password = input("Please enter your password: ")

if usernameOrEmail == username1:
    print(password)
    if password == password1:
        print("Welcome again " + username1 + " sexy motherfuc*er")
    else:
        print("Wrong answer. Forgot your password?\nYes?\n\nGame over\n\nYou should write it down next time.")
elif usernameOrEmail == email1:
    print(password)
    if password == password1:
        print("Welcome again " + username1 + "you motherfuc*er")
    else:
        print("Wrong answer. Forgot your password?\nYes?\nGame over\nYou should write it down next time.")
else:
    print("Wrong data, I saw that coming. Please try again")
    usernameOrEmail = input("Please enter your username or email: ")



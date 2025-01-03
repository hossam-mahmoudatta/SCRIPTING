
def welcomeMsg():
    print("\nWelcome to Hosa Crowd Funding App:")

def showMainMenu():
    print("\nMENU:")
    print("1. Create an Account")
    print("2. Already a user? Sign in.")
    print("3. Exit")

def mainMenu():
    menuItems = []  # List to store items
    while True:
        showMainMenu()
        choice = input("Enter your choice: ")
        
        if choice == 1:
            print("You'll sign up now.")
        elif choice == 2:
            print("You can sign in now.")
        elif choice == 3:
            print("You'll exit now.")
            break
        else:
            print("Invalid Choice")

# Run the program
welcomeMsg()
mainMenu()

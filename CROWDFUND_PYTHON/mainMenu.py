# Hossam Mahmoud
# Creating a Crowd Funding Application

from signUp import *

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
        if choice == '1':
            print("\nYou'll sign up now.")
            signUpMsg()
            signUpAPI()
        elif choice == '2':
            print("\nYou can sign in now.")
        elif choice == '3':
            print("\nYou'll exit now.")
            break
        else:
            print("\nInvalid Choice")

# Run the program
welcomeMsg()
mainMenu()
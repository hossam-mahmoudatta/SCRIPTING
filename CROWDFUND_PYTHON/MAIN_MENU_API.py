# Hossam Mahmoud
# Creating a Crowd Funding Application

from SIGN_UP_API import *
from SIGN_IN_API import *

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
        choice = input("\nEnter your choice: ")
        if choice == '1':
            print("\nYou'll be directed to the sign up page...")
            signUpMsg()
            signUpAPI()
        elif choice == '2':
            print("\nYou'll be directed to the sign in page...")
            signInMsg()
            signInAPI()
        elif choice == '3':
            print("\nYou'll exit now.")
            print("\nHave a nice day!")
            break
        else:
            print("\nInvalid Choice")

# Run the program
welcomeMsg()
mainMenu()
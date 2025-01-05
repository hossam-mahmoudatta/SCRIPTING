# Hossam Mahmoud
# Creating a Crowd Funding Application

from SIGN_UP_API import *
from SIGN_IN_API import *

def dashboardMsg():
    print("\nHosa Crowd Funding App\nDashboard")

def showMainMenu():
    print("\nMENU:")
    print("1. Create a Project")
    print("2. View Project")
    print("3. Edit Project")
    print("4. Delete Project")
    print("5. Search")
    print("6. Back to Main Menu")

def mainMenu():
    menuItems = []  # List to store items
    while True:
        showMainMenu()
        choice = input("Enter your choice: ")
        if choice == '1':
            print("\nYou'll be directed to setup your project...")
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
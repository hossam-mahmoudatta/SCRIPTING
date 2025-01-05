# Hossam Mahmoud
# Creating a Crowd Funding Application

from VERIFICATION_APIs import *
from FILE_HANDLING_APIs import *
from DASHBOARD import *

def signInMsg():
    print("\nHosa Crowd Funding App\nSign In Page")

def signInAPI():
    print("\nEnter your Login Info:")
    # Checks if the user that i will create exists or not.
    existingUsers = readUserDB()
    
    while True:
        userName = input("Username: ")
        if userName in existingUsers:
            print("Username Valid! Enter your Password now:\n")
            
            while True:
                userPassword = input("Password: ")
                if existingUsers[userName]['password'].strip() == userPassword:
                    print("Login Successful!")
                    userData = existingUsers[userName]
                    userDashboard(userData)
                    # break
                else:
                    print("Error: Incorrect Password. Please try again.")
        else:
            print("Username doesn't exist! Try again.\n")

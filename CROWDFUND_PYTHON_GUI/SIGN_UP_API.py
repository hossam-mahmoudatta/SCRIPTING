# Hossam Mahmoud
# Creating a Crowd Funding Application

from VERIFICATION_APIs import *
from USER_HANDLING_APIs import *

###########################################
###########################################

def signUpMsg():
    print("\nHosa Crowd Funding App\nSign Up Page")

###########################################
###########################################

def signUpAPI():
    print("\nAdd User Info:")
    # Checks if the user that i will create exists or not.
    existingUsers = readUserDB()
    userID = generateUserID()
    
    while True:
        userName = input("Enter a Unique Username: ")
        if userName in existingUsers:
            print("Error: Username already exists. Please choose a different one.")
        else:
            break
        
    while True:
        userEmail = verifyEmail("Enter Email: ")
        if any(user['email'] == userEmail for user in existingUsers.values()):
            print("Error: Email already exists. Please choose a different one.")
        else:
            break    
    
    userFName = verifyString("Enter First Name: ")
    userLName = verifyString("Enter Last Name: ")
    userPassword = verifyPassword("Enter your Password: ")
    userMobile = verifyMobile("Enter your Phone Number: ")
    
    userData = {
        "id": userID,
        "fname": userFName,
        "lname": userLName,
        "user": userName,
        "email": userEmail,
        "password": userPassword,
        "mobile": userMobile,
        "projects": []
    }
    
    print(f"\nUser: {userName} has been successfully registered!")
    print("\nGenerated User ID: ", userID)
    print("\n", userData)
    
    # I need to save the data to a file
    saved = saveUserDB(userData)
    if saved:
        print("----------User Info Saved!----------")

###########################################
###########################################
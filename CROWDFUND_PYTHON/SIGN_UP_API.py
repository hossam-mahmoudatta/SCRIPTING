# Hossam Mahmoud
# Creating a Crowd Funding Application

from VERIFICATION_APIs import *
from FILE_HANDLING_APIs import *

def signUpMsg():
    print("\nHosa Crowd Funding App\nSign Up Page")

def signUpAPI():
    print("\nAdd User Info:")
    userFName = verifyString("Enter First Name: ")
    userLName = verifyString("Enter Last Name: ")
    userEmail = verifyEmail("Enter Email: ")
    userPassword = verifyPassword("Enter your Password: ")
    userMobile = verifyMobile("Enter your Phone Number: ")
    
    userData = {
        "id": generateUserID(),
        "fname": userFName,
        "lname": userLName,
        "email": userEmail,
        "password": userPassword,
        "mobile": userMobile
    }
    
    print(userData)
    # I need to save the data to a file
    
    # saved = save_book(bookdata)
    # if saved:
    #     print("----------User Info Saved!----------")

# Hossam Mahmoud
# Creating a Crowd Funding Application

from helperAPIs import *

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
        "id": generate_id(),
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
        


# def mainMenu():
#     menuItems = []  # List to store items
#     while True:
#         showMainMenu()
#         choice = input("Enter your choice: ")
#         if choice == '1':
#             print("\nYou'll sign up now.")
#         elif choice == '2':
#             print("\nYou can sign in now.")
#         elif choice == '3':
#             print("\nYou'll exit now.")
#             break
#         else:
#             print("\nInvalid Choice")
                
#         # if choice.isdigit():
#         #     choice = int(choice)


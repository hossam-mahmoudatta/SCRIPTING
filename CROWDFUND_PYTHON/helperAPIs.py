# Helper methods for validation

import re

def verifyInt(message="Please enter number:"):
    while True:
        try:
            inputNumber = int(input(message))
            return inputNumber
        except errorValue: # type: ignore
            print("Invalid input! Please enter a valid integer.")


def verifyString(message="Please enter string:"):
    while True:
        inputString = input(message)
        if inputString.isalpha():
            return inputString
        else:
            print("Invalid input! Please enter a valid string.")
            

def verifyEmail(message="Please enter a valid email:"):
    emailPattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    while True:
        userEmail = input(message)
        if re.match(emailPattern, userEmail):
            return userEmail
        else:
            print("Invalid email! Please enter a valid email address.")
            

def verifyPassword(message="Enter your password: ", confirmMessage="Confirm your password: "):
    while True:
        password = input(message)
        confirmPassword = input(confirmMessage)
        
        if password == confirmPassword:
            print("Password confirmed successfully!")
            return password
        else:
            print("Passwords do not match. Please try again.")


# Helper methods for validation

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

        print("--- please enter a string --- ")
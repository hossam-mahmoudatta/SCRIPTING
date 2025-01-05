
import json, os, datetime

USER_ID_DB = 'USER_ID_DB.json'

# Load existing user ID data from the file (if it exists)
def readUserID():
    if os.path.exists(USER_ID_DB):
        # Read about benefits of using with .. as
        with open(USER_ID_DB, 'r') as file:
            return json.load(file)
    else:
        return {}


# Save the updated user ID data to the file
def saveUserID(userID):
    with open(USER_ID_DB, 'w') as file:
        json.dump(userID, file, indent=4)
        
        
def generateUserID(username):
    # Load the existing user IDs
    currentUserIDs = readUserID()
    
    # Get today's date in YYYYMMDD format
    todayDate = datetime.datetime.now().strftime("%Y%m%d")
    
    # Initialize the count for today's date if not already present
    if todayDate not in currentUserIDs:
        currentUserIDs[todayDate] = 1
    else:
        currentUserIDs[todayDate] += 1
    
    # Generate the ID by combining the date and the user number
    userNumber = str(currentUserIDs[todayDate]).zfill(3)  # Pads the number with leading zeros
    userID = f"{todayDate}{userNumber}"
    
    # Save the updated user ID data
    saveUserID(currentUserIDs)
    
    # Return the unique ID
    return userID

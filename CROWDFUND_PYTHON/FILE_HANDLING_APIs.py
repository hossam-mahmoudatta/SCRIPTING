
import json, os, datetime

###############################################
# Setting the path where the DBs will be created
PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(PROJECT_DIR, 'DATABASES')

# Ensure the "databases" folder exists
os.makedirs(DB_DIR, exist_ok=True)

USER_ID_DB = os.path.join(DB_DIR, 'USER_ID_DB.json')
USER_DB = os.path.join(DB_DIR,  'USER_DB.json')
###############################################
# Load existing user ID data
def readUserID():
    if os.path.exists(USER_ID_DB):
        with open(USER_ID_DB, 'r') as file:
            return json.load(file)
    else:
        return {}


# Save the updated user ID data
def saveUserID(userIDData):
    with open(USER_ID_DB, 'w') as file:
        json.dump(userIDData, file, indent=4)


def generateUserID():
    # Load existing user ID data
    userIDData = readUserID()
    
    # Get today's date in YYYYMMDD format
    todayDate = datetime.datetime.now().strftime("%Y%m%d")
    
    # Initialize the count for today's date if not already present
    if todayDate not in userIDData:
        userIDData[todayDate] = 1
    else:
        userIDData[todayDate] += 1
    
    # Generate the ID by combining the date and the user number
    userNumber = str(userIDData[todayDate]).zfill(3)  # Pads the number with leading zeros
    userID = f"{todayDate}{userNumber}"
    
    # Save the updated user ID data
    saveUserID(userIDData)
    
    # Return the unique ID
    return userID

###############################################
###############################################

# Load existing user ID data from the file (if it exists)
def readUserDB():
    if os.path.exists(USER_DB):
        # Read about benefits of using with .. as
        with open(USER_DB, 'r') as file:
            return json.load(file)
    else:
        return {}

# Save the updated user ID data to the file
def saveUserDB(userData):
    existingUsers = readUserDB()
    # Use the username as the key
    existingUsers[userData['user']] = userData
    with open(USER_DB, 'w') as file:
        json.dump(existingUsers, file, indent=4)

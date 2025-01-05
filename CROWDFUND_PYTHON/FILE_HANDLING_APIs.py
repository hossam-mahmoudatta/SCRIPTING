
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
    user_ids_per_date = load_user_ids()
    
    # Get today's date in YYYYMMDD format
    todayDate = datetime.datetime.now().strftime("%Y%m%d")
    
    # Initialize the count for today's date if not already present
    if today_date not in user_ids_per_date:
        user_ids_per_date[today_date] = 1
    else:
        user_ids_per_date[today_date] += 1
    
    # Generate the ID by combining the date and the user number
    user_number = str(user_ids_per_date[today_date]).zfill(3)  # Pads the number with leading zeros
    user_id = f"{today_date}{user_number}"
    
    # Save the updated user ID data
    save_user_ids(user_ids_per_date)
    
    # Return the unique ID
    return user_id

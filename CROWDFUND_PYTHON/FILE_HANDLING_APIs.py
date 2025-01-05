
import json, os, datetime

USER_ID_DB = 'USER_ID_DB.json'

# Load existing user ID data from the file (if it exists)
def load_user_ids():
    if os.path.exists(USER_ID_FILE):
        with open(USER_ID_FILE, 'r') as file:
            return json.load(file)
    else:
        return {}

# Save the updated user ID data to the file
def save_user_ids(user_ids):
    with open(USER_ID_FILE, 'w') as file:
        json.dump(user_ids, file, indent=4)

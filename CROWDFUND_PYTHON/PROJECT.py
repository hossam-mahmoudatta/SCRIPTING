
import json, os, datetime

###############################################
# Setting the path where the DBs will be created
MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(MAIN_DIR, 'DATABASES')

# Ensure the "databases" folder exists
os.makedirs(DB_DIR, exist_ok=True)

PROJECT_ID_DB = os.path.join(DB_DIR, 'PROJECT_ID_DB.json')
PROJECT_DB = os.path.join(DB_DIR,  'PROJECT_DB.json')
###############################################
# Load existing user ID data
def readProjectID():
    if os.path.exists(PROJECT_ID_DB):
        with open(PROJECT_ID_DB, 'r') as file:
            return json.load(file)
    else:
        return {}


# Save the updated user ID data
def saveProjectID(projectIDData):
    with open(PROJECT_ID_DB, 'w') as file:
        json.dump(projectIDData, file, indent=4)


def generateProjectID():
    # Load existing user ID data
    projectIDData = readProjectID()
    
    # Get today's date in YYYYMMDD format
    todayDate = datetime.datetime.now().strftime("%Y%m")
    
    # Initialize the count for today's date if not already present
    if todayDate not in projectIDData:
        projectIDData[todayDate] = 1
    else:
        projectIDData[todayDate] += 1
    
    # Generate the ID by combining the date and the user number
    projectNumber = str(projectIDData[todayDate]).zfill(3)  # Pads the number with leading zeros
    projectID = f"{todayDate}{projectNumber}"
    
    # Save the updated user ID data
    saveProjectID(projectIDData)
    
    # Return the unique ID
    return projectID

###############################################
###############################################
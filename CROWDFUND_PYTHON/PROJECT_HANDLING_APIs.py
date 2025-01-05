# Hossam Mahmoud
# Creating a Crowd Funding Application

from VERIFICATION_APIs import *
from USER_HANDLING_APIs import *

###########################################
###########################################

def projectMsg():
    print("\nHosa Crowd Funding App\nInitiate a Project")

###########################################
###########################################

def createProject(userData):
    print("\nAdd Project Info:")
    # print(userData) 
    
    # Ask for project details
    projectTitle = input("Enter Project Title: ")
    projectDescription = input("Enter Project Description: ")
    projectFund = float(input("Enter Target Fund: "))
    projectStartDate = input("Enter Project's Start Date (YYYY-MM-DD): ")
    projectEndDate = input("Enter Project's End Date (YYYY-MM-DD): ")
    
    # Create the new project with an ID (incremental)
    projectID = len(userData["projects"]) + 1  # Create an incremental ID
    projectData = {
        "id": projectID,
        "title": projectTitle,
        "description": projectDescription,
        "target_fund": projectFund,
        "start_date": projectStartDate,
        "end_date": projectEndDate
    }
    
    # Add the new project to the user's projects list
    userData["projects"].append(projectData)

    # Save the updated user data to the file
    saveUserDB(userData)

    print(f"\nProject '{projectTitle}' added successfully!")

###########################################
###########################################

def listProjects(userData):
    if userData["projects"]:
        for project in userData["projects"]:
            print(f"""
                #########################\n
                ID: {project['id']}\n
                Title: {project['title']}\n
                Description: {project['description']}\n
                Target Fund: {project['target_fund']}\n
                Start Date: {project['start_date']}\n
                End Date: {project['end_date']}\n
                #########################\n""")
    else:
        print("No projects were found.")

###########################################
###########################################

def editProject(userData):
    # Checks if this user has any projects or not
    if not userData["projects"]:
        print("No projects found.")
        return
    
    print("\nSelect a project to edit:\n")
    for project in userData["projects"]:
        print(f"ID: {project['id']} - Title: {project['title']}")
    
    # Get the project ID to edit
    try:
        projectID = int(input("\nEnter project ID to edit: "))
        project = None
        for proj in userData["projects"]:
            if proj["id"] == projectID:
                project = proj
                break
        
        # Prompts the user which field they want to edit
        print(f"Editing Project: {project['title']}\n")
        project['title'] = input(f"Enter new title (current: {project['title']}): ") or project['title']
        project['description'] = input(f"Enter new description (current: {project['description']}): ") or project['description']
        project['target_fund'] = float(input(f"Enter new target fund (current: {project['target_fund']}): ") or project['target_fund'])
        project['start_date'] = input(f"Enter new start date (current: {project['start_date']}): ") or project['start_date']
        project['end_date'] = input(f"Enter new end date (current: {project['end_date']}): ") or project['end_date']
        
        # Save the updated user data
        saveUserDB(userData)
        
        # Printing the newly added project
        print(f"""
                #########################\n
                ID: {project['id']}\n
                Title: {project['title']}\n
                Description: {project['description']}\n
                Target Fund: {project['target_fund']}\n
                Start Date: {project['start_date']}\n
                End Date: {project['end_date']}\n
                #########################\n""")
        
        # Confirms the newly updated project
        print(f"\nProject '{project['title']}' updated successfully!")
    
    except ValueError:
        print("Invalid input. Please enter a valid Project ID.")

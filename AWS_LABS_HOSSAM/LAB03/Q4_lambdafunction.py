import boto3  # Imports the AWS SDK for Python (Boto3) to interact with AWS services

# Initialize the S3 client to communicate with Amazon S3
s3 = boto3.client("s3")

# Define the name of the destination S3 bucket
bucket_name = "hossam-destinationbucket"

# Define the file path for temporary storage inside the Lambda environment
# AWS Lambda only allows writing to the "/tmp/" directory, which has a 512MB limit
file_name = "/tmp/hosa-test-file.txt" 

def lambda_handler(event, context):
    # AWS Lambda function to create a text file and upload it to an S3 bucket.
    
    try:
        # Step 1: Create a simple text file in the temporary "/tmp/" directory
        with open(file_name, "w") as file:
            file.write("Hello Hossam, I'm Lambda.")  # Write text to the file

        # Step 2: Upload the file from "/tmp/" to the S3 bucket
        # The file will be saved in S3 as "hosa-test-file.txt" (without the /tmp/ path)
        s3.upload_file(file_name, bucket_name, "hosa-test-file.txt")

        # Print confirmation message (appears in AWS Lambda logs)
        print(f"File successfully uploaded to {bucket_name}/hosa-test-file.txt")
        
        # Step 3: Return a success response
        return {
            "status": "Success",      # Status message
            "file": "hosa-test-file.txt"  # Name of the uploaded file in S3
        }
    
    except Exception as e:
        # Print the error message in AWS Lambda logs if something goes wrong
        print(f"Error: {e}")

        # Step 4: Return an error response if the file upload fails
        return {
            "status": "Error",
            "message": str(e)  # Convert error message to a string for response
        }

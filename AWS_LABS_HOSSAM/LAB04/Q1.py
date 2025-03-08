import boto3
import json

# Initialize S3 client
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table()

# Define source and destination bucket names
SOURCE_BUCKET = "hossam-sourcebucket"
DESTINATION_BUCKET = "hossam-destinationbucket"

def lambda_handler(event, context):
    try:
        # Get file name from request
        file_name = event["queryStringParameters"]["file_name"]
        
        # Copy file from source bucket to destination bucket
        copy_source = {'Bucket': SOURCE_BUCKET, 'Key': file_name}
        s3.copy_object(Bucket=DESTINATION_BUCKET, Key=file_name, CopySource=copy_source)

        print(f"File '{file_name}' copied from {SOURCE_BUCKET} to {DESTINATION_BUCKET}")

        return {
            "statusCode": 200,
            "body": f"File '{file_name}' successfully copied to {DESTINATION_BUCKET}"
        }

    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }

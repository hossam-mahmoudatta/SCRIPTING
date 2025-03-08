import boto3

# Initialize S3 client
s3 = boto3.client("s3")

# Define source and destination bucket names
SOURCE_BUCKET = "hossam-sourcebucket"
DESTINATION_BUCKET = "hossam-destinationbucket"
TABLE_NAME = "dynamoDB-HosaLambda"

def lambda_handler(event, context):
    try:
        # Get file name from request
        record = event["Records"][0]
        file_name = record["s3"]["object"]["key"]
        
        # Copy file from source bucket to destination bucket
        s3.copy_object(
            CopySource={"Bucket": SOURCE_BUCKET, "Key": file_name},
            Bucket=DESTINATION_BUCKET,
            Key=file_name, 
        )

        print(f"File '{file_name}' copied from {SOURCE_BUCKET} to {DESTINATION_BUCKET}")

        # Update DynamoDB table
        table = dynamodb.Table(TABLE_NAME)

        table.put_item(
            Item={
                "name": file_name,
                "source": SOURCE_BUCKET,
                "message": DESTINATION_BUCKET
            }
        )


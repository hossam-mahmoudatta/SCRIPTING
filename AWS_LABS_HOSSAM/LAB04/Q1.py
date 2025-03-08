import boto3
import json

# Initialize S3 client
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb").Table("dynamoDB-HosaLambda")
destination_bucket = "hossam-destinationbucket" 

def lambda_handler(event, context):
    print("Received event:", json.dumps(event, indent=2))  # Debugging line

    if "Records" not in event:
        return {"statusCode": 400, "body": json.dumps("Invalid event format")}
    
    for record in event["Records"]:
        source_bucket = record["s3"]["bucket"]["name"]
        file_name = record["s3"]["object"]["key"]
        
        # Copy file to destination bucket
        s3.copy_object(
            Bucket=destination_bucket,
            Key=file_name,
            CopySource= {"Bucket": source_bucket, "Key": file_name},
        )
        
        dynamodb.put_item(
            Item = {
                "file_name": file_name,
                "source_bucket": source_bucket,
                "destination_bucket": destination_bucket
                }
        )
        print(f"File {file_name} added to DynamoDB from {source_bucket}")
    
    return {"StatusCode": 200, "body": json.dumps("Success")}
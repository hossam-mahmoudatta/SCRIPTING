import boto3
import json

# Initialize S3 client
s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("dynamoDB-HosaLambda")

def lambda_handler(event, context):
    for record in event["Records"]:
        bucket = record["s3"]["bucket"]["name"]
        file_name = record["s3"]["object"]["key"]
        
        table.put_item(Item={"file_name": file_name, "bucket": bucket})
        print(f"File {file_name} added to DynamoDB from {bucket}")
    
    return {"StatusCode": 200, "body": json.dumps("Success")}
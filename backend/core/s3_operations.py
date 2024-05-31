import boto3
from botocore.exceptions import ClientError

# debug
import logging

# to upload file
def upload_file(file_name: str, bucket: str):
    
    print("inside function")
    
    object_name: str = file_name
    
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        print(response)
    
    except ClientError as e:
        print(e)
        logging.error(e)
        


upload_file("bhanupratapCV.pdf", "prataptech-guardian")

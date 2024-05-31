import boto3
from botocore.exceptions import ClientError
import uuid

# user defined
from s3_responses import S3Response


# to upload file
def upload_file(file_name: str, bucket: str) -> S3Response:
    object_name: str = str(uuid.uuid1())
    
    try:
        s3_client = boto3.client('s3')
        response = s3_client.upload_file(file_name, bucket, object_name)
        return S3Response(status=False, desc=object_name)
        
        
    except ClientError as e:
        return S3Response(status=False, desc=str(e))
        


# to download file 
def download_file(file_name: str, bucket: str, object_name: str):
    try:
        s3_client = boto3.client("s3")
        response = s3_client.download_file(bucket, object_name, object_name)
        print(response)
    except Exception as e:
        print(e)
        

# upload_file("bhanupratapCV.pdf", "prataptech-guardian")
# 6557885e-1f24-11ef-848b-8298d9ac4759

# download_file("6557885e-1f24-11ef-848b-8298d9ac4759", "prataptech-guardian", "6557885e-1f24-11ef-848b-8298d9ac4759")
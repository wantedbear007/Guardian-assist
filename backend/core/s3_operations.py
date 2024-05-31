import boto3
from botocore.exceptions import ClientError
import uuid

# user defined
from core.s3_responses import S3Response


# to upload file
def upload_file(file, bucket: str) -> S3Response:
    object_name: str = str(uuid.uuid1()) + ".pdf"
    
    try:
        s3_client = boto3.client('s3')
        s3_client.upload_fileobj(file.file, bucket, object_name)
        
        url = s3_client.generate_presigned_url(
            "get_object", Params={"Bucket": bucket, 'Key': object_name}, ExpiresIn=3600
        )
        return S3Response(status=False, desc=url)
    
    
        
    except ClientError as e:
        return S3Response(status=False, desc=str(e))
        


# to download file 
def download_file(bucket: str, object_name) -> S3Response:
    
    try:
        s3_client = boto3.client("s3")
        response = s3_client.download_file(bucket, object_name, object_name)
        return S3Response(status=True, desc="success")
    
    except Exception as e:
        print(e)
        return S3Response(status=False, desc=f"Database error {str(e)}")
        
        


# upload_file("bhanupratapCV.pdf", "prataptech-guardian")
# 6557885e-1f24-11ef-848b-8298d9ac4759

# download_file( "prataptech-guardian","590f1d38-1f37-11ef-b7b3-8298d9ac4759")
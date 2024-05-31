from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import os

# defined
from utils.file_utils import allowed_file_types;
from core.s3_responses import S3Response
from core.s3_operations import upload_file, download_file
from utils.constants import BUCKET, MAX_FILE_SIZE



app = FastAPI()


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Todo
# add pre-endpoint i.e /v1/upload

url: str = "/v1"


@app.get("/")
async def root():
    return {
        "time": datetime.now().isoformat(),
        "message": "Guardian servers are working.",
        "author": "@wantedbear007"
    }

    

@app.post('/upload/')
async def upload(file: UploadFile | None = None):
    
    
    # validators
    if file is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No file found.")
    
    if not allowed_file_types(file.filename):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not allowed")    
    
    if file_size > MAX_FILE_SIZE:
        raise HTTPException(status_code=status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, detail="Max 1 MB file allowed")

    
    # uploading
    file_upload: S3Response = upload_file(file_name=file.filename, bucket=BUCKET);
    if not file_upload.status:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to upload file")
    
    
    return {
        "message" : "File successfully uploaded",
        "file_id": file_upload.desc
    }
    
    
    
        
        
    
        
        
        
    


    

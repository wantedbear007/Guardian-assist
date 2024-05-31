from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
import uvicorn

# defined
from utils.file_utils import allowed_file_types;
from core.s3_responses import S3Response
from core.s3_operations import upload_file, download_file
from utils.constants import BUCKET, MAX_FILE_SIZE
from model.chat_req_model import ChatModel
from core.chat_handler import handle_query



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
# add rate limiter

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
    
    # uploading
    file_upload: S3Response = upload_file(file=file, bucket=BUCKET);
    if not file_upload.status:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Failed to upload file")
    
    
    return {
        "message" : "File successfully uploaded",
        "file_id": file_upload.desc
    }
    
    
@app.post('/chat/')
async def chat(item: ChatModel):
    if not item.doc_url or not item.query:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="All fields required")
    
    if len(item.query) > 80:
        raise HTTPException(status_code=status.HTTP_414_REQUEST_URI_TOO_LONG, detail="Query too long")
    
    
    response: S3Response = handle_query(doc_url=item.doc_url, query=item.query)
    
    if response.status == False:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error")
    
    return {
        "message" : "success",
        "response" : response.desc,
    }    
    
        
    # print(len(item.query))
    
    # return {"message": "fixed"}
    
    
if __name__ == "__main__":
    uvicorn.run(app='main:app', reload=True)
    
        
        
    
        
        
        
    


    

from fastapi import FastAPI, File, UploadFile, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime

# defined
from utils.file_utils import allowed_file_types;

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
async def upload(file: UploadFile = File(...)):
    
    
    # validators
    if file is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No file found.")
    
    if not allowed_file_types(file.filename):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="File type not allowed")
    
    
        
        
    return {"no error": file.filename}
    
        
        
        
    


    

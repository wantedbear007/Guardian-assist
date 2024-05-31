from pydantic import BaseModel

class ChatModel(BaseModel):
    doc_url: str
    query: str
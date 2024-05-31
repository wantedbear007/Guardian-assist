
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
import getpass
import requests
from io import BytesIO
from typing_extensions import Concatenate
from langchain.chains.question_answering import load_qa_chain
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv

# user defined
from core.s3_responses import S3Response


file_url = "https://prataptech-guardian.s3.amazonaws.com/c30643ca-1f63-11ef-a149-8298d9ac4759.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAZQ3DPEE7NKOHXSFU%2F20240531%2Fap-south-1%2Fs3%2Faws4_request&X-Amz-Date=20240531T153801Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=bad73577dd0d639242ba8247ad1587e89ae24d27286822cc1c4d7d0e1c604fb8"



def handle_query(doc_url: str, query: str):
    try:
        load_dotenv()
        # to get pdf data
        response = requests.get(doc_url)
        response.raise_for_status()

        pdf_file = BytesIO(response.content)

        pdf_reader = PdfReader(pdf_file)
        
        
        # to extract text from multiple pages
        text = ''

        for i, page in enumerate(pdf_reader.pages):
            content = page.extract_text()

            if content:
                text += content
        
        # dividing into chunks
        splitter_text = CharacterTextSplitter(
        separator = '\n',
        chunk_size = 800,
        chunk_overlap = 200,
        length_function = len
        )

        texts = splitter_text.split_text(text)
        
        google_api_key = os.getenv("GOOGLE_API_KEY")
        if not google_api_key:
            google_api_key = getpass("Enter your Google API key");
            os.environ["GOOGLE_API_KEY"] = google_api_key
        
  

        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        doc_search = FAISS.from_texts(texts, embeddings);
        # llm = ChatGoogleGenerativeAI(model="gemini-pro")
        llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest")
        #
        chain = load_qa_chain(llm, chain_type="stuff")
        
        # query = "what is the qualification "
        docs = doc_search.similarity_search(query)
        res = chain.run(input_documents=docs, question=query)
        
        return S3Response(status=True, desc=res);

        
        
    except Exception as e:
        return S3Response(status=False, desc=str(e))
        # print("error occurred")
        # print(e)
        
    
# handle_query(file_url, "name of student")
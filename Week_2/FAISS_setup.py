# faiss-cpu
# faiss-gpu

from langchain_core.documents import Document 
from langchain_google_genai import GoogleGenerativeAIEmbeddings 
from langchain_community.vectorstores import FAISS 
import os 

#1. secure authentication 
api_key = os.getenv("GEMINI_API_KEY")

#2. Initialize the Google Embedding Model 
embedder = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key = api_key
)

print("Initialized the embedding model")

#3. Simulate our chunked, metadata-rich documents from Session 1.3 

chunks = [
    Document(
        page_content="Tony has proposed moving to a distributed architecture to handle the load of 500 PDFs.",
        metadata={"source": "Extract_Once_Audit.pdf", "chapter": "Engineering", "chunk_id": "CHK-001"}
    ),
    Document(
        page_content="Marten noted a critical issue: 15% of scanned PDF documents are failing the OCR pipeline.",
        metadata={"source": "Extract_Once_Audit.pdf", "chapter": "Compliance", "chunk_id": "CHK-002"}
    ),
    Document(
        page_content="Jaymin is leading the budget review. The estimated cost for Q1 scaling is $45,000.",
        metadata={"source": "Extract_Once_Audit.pdf", "chapter": "Financials", "chunk_id": "CHK-003"}
    ),
    Document(
        page_content="The annual company retreat will be held in Hawaii this year, featuring surfing lessons.",
        metadata={"source": "HR_Memo.pdf", "chapter": "Culture", "chunk_id": "CHK-004"}
    )
]

print("[System] Simulated Document Chunks Loaded. Ready for FAISS Integration.")

print("Initializing the FAISS Vector Database....\n")

# This line of code is doing millions of mathematical operations. 
# It creates the index  and populates it with our embedded documents
vectorstore = FAISS.from_documents(documents = chunks, embedding = embedder)

print("[Success] FAISS Index built and populated in RAM")

# The User's query

query = "How much money do we need to fix the pipeline?"

print(f"Executing ANN Vector Search for : '{query}'\n")

# we perform the search, asking for the top 2 closest vectors(k=2)
# FAISS embeds the query, calculates the cosine distance in the graph, and 
# returns the matches
results = vectorstore.similarity_search(query, 2)

print("=====SEARCH RESULTS======")

for i, doc in enumerate(results):
    print(f"\n[Match #{i+1}]")
    print(f"Content: {doc.page_content}")
    print(f"Retrieved Metadata: {doc.metadata}")


#Define the folder name where we want to save our database files 
DB_DIR = "faiss_extract_once_db"

print(f"\nSerializing FAISS index to disk at ./{DB_DIR}...")

#save the index. This creates the .faiss and .pkl files 
vectorstore.save_local(DB_DIR)

#verify the files were created 
print("Listing files in the directory")
print(os.listdir(DB_DIR))

print("\nSimulating server restart...")
#Delete the in-memomy 
del vectorstore

print("Loading FAISS index directly from hard drive...\n")

#We must explcitly allow dangerous deserialization.
# Pickle files can execute malicious code if you donwload them from an untrusted source. 
# Because we created it locally, it is 100% safe to load
restored_db = FAISS.load_local(
    folder_path= DB_DIR,
    embeddings = embedder,
    allow_dangerous_deserialization= True
)

restored_results = restored_db.similarity_search("Why are documents failing?", k =1)

print ("====RESTORED DATABSE SEARCH====")
print(f"Content: {restored_results[0].page_content}")
print(f"Metadata: {restored_results[0].metadata}")
print("\n [System] Pipeline Complete. The index is fully")
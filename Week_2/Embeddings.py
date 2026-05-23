import numpy as np 
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import os


#secuely fetching the API key
api_key = os.getenv("GEMINI_API_KEY")

#initialize the embedding model (not a chat model)
embedder = GoogleGenerativeAIEmbeddings(
    model = "models/gemini-embedding-001",
    google_api_key = api_key
)

print("[System] 768- Dimensional Google Embedding Model Initialized!")

# Define our text data
s1 = "Tony and Marten are scaling the data pipeline to handle more corporate PDFs."
s2 = "The engineering team is upgrading the document ingestion architecture to increase throughput."
s3 = s1 + " " + s1 + " " + s1 + " " + s1 + " " + s1  # Artificial length inflation
s4 = "The client was incredibly happy with the new chocolate cake recipe."
s5 = "Tony and Marten are NOT scaling the data pipeline."

print("Translating human text into mathematical vectors via API...\n")

# convert text to vectors 
v1 = np.array(embedder.embed_query(s1))
v2 = np.array(embedder.embed_query(s2))
v3 = np.array(embedder.embed_query(s3))
v4 = np.array(embedder.embed_query(s4))
v5 = np.array(embedder.embed_query(s5))

print(f"Total Dimensions per vector: {len(v1)}")
print(f"Sample of Vector 1 (first 5 dims): {v1[:5]}\n")

def calc_cosine(vec_a, vec_b):
    dot_product = np.dot(vec_a, vec_b)
    norm_a = np.linalg.norm(vec_a)
    norm_b = np.linalg.norm(vec_b)

    return dot_product/(norm_a* norm_b)

def euclidean(vec_a, vec_b):
    return np.linalg.norm(vec_a - vec_b)

print("="*60)
print(" SEMANTIC SEARCH ALGEBRA LABORATORY ")
print("="*60 + "\n")


print("v1 vs v2")
print(f"Cosine Similarity: {calc_cosine(v1,v2):.4f}\n") # Very High -- Meaning is captured
print(f"Euclidean dist: {euclidean(v1,v2):.4f}\n")


print("v1 vs v3")
print(f"Cosine Similarity: {calc_cosine(v1,v3):.4f}\n") 
print(f"Euclidean dist: {euclidean(v1,v3):.4f}\n")



print("v1 vs v4")
print(f"Cosine Similarity: {calc_cosine(v1,v4):.4f}\n") 
print(f"Euclidean dist: {euclidean(v1,v4):.4f}\n")

print("v1 vs v5")
print(f"Cosine Similarity: {calc_cosine(v1,v5):.4f}\n") 
print(f"Euclidean dist: {euclidean(v1,v5):.4f}\n")
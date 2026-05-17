from fpdf import FPDF 
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size =12)

report_text = """
Extract Once, Judge Many - Q4 Infrastructure Report
Document ID: DOC-99482
Date: November 2026

--- SECTION 1: INGESTION BOTTLENECKS ---
Over the past quarter, we have seen significant bottlenecks in the data ingestion phase. 
Tony has proposed moving to a distributed architecture to handle the load. The current 
single-node setup is failing when we attempt to process more than 500 PDFs per hour.

--- SECTION 2: COMPLIANCE AND OCR ---
In terms of compliance, Marten noted a critical issue during the Tuesday review. 
Exactly 15% of our scanned PDF documents are failing the OCR (Optical Character Recognition) pipeline 
because of low DPI scans from the legacy branch offices. We must address this before scaling 
the pipeline to the European division.

--- SECTION 3: BUDGET ALLOCATION ---
Jaymin is leading the budget review for these necessary infrastructure upgrades. 
The estimated cost for Q1 scaling will be approximately $45,000. Because this exceeds 
the standard departmental threshold, it will require VP approval by Friday.
"""
pdf.multi_cell(0,10, txt = report_text)
file_name = "Extract_Once_Audit.pdf"
pdf.output(file_name)

print(f"[System] Dummy PDF '{file_name}' generated successfully. Ready for ingestion")


Phase 1

loader = PyPDFLoader("Extract_Once_Audit.pdf")
pages = loader.load() # python object from pdf

print(f"Raw metadata from Page 1: {pages[0].metadata}")

# Phase 2 
# Configure the recursive splitter 

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 300,
    chunk_overlap = 80,
    length_function = len,# We tell it to count characters, not words ,
    separators= ["\n\n", "\n", " ", ""] # paragraphs first, then lines, words, characters
)

# Phase 3 
chunks = text_splitter.split_documents(pages)
print(f"[Phase 3] Successfully shattered the document into {len(chunks)}) overlapping chunks.\n")

# Phase 4 : Metadata Tagging 

for i, chunk in enumerate(chunks):
    chunk.metadata['chunk_id']= f"CHK--{i+1:03d}" # CHK--001

    chunk.metadata["project_name"]= "Extract Once, Judge Many"

    if "BUDGET" in chunk.page_content:
        chunk.metadata["category"] = "Financials"
    elif "COMPLIANCE" in chunk.page_content:
        chunk.metadata["category"] = "Legal/Compliance"
    elif "BOTTLENECKS" in chunk.page_content:
        chunk.metadata["category"] = "Engineering"
    else:
        chunk.metadata["category"] = "General Overview"

print("="*50)
print("FINAL CHUNK INSPECTION")
print("="*50)

for chunk in chunks[0:4]:
    print(f"\n[{chunk.metadata['chunk_id']}] Category: {chunk.metadata['category']}")
    print("-"* 40)
    print(f"Text content: \n{chunk.page_content}")
    print("-"*40)
    print(f"Full Attached Metadata: {chunk.metadata}")

print("\n[System] Pipeline complete. Data is ready for Vetor Database insertion.")
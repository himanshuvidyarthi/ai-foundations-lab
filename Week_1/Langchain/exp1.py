#create a pdf 
    #add pages and content to the pdf 

#use langchain to generate chunks of content of the pdf 

#create and assign meta data to each chunk 

#visualize the chunking 

# 1) import the libraries 

from fpdf import FPDF 
from langchain_community.document_loaders import PyPDFLoader

#) 2) Create a sample pdf 
pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 12) 

text = """
    Company Report - Q4

    Tony is leading the infrastructure team. 
    The total budget allocated is $50,000. 
    Compliance issues were found in 15% of documents.
"""

pdf.multi_cell(0,10,text)
pdf.output("sample.pdf")

print("PDF generated successfully!")

#3) Langchain process starts here 

print(" Langchain process starts here")

#4) Load the PDF using Langchain 

loader = PyPDFLoader("file-example_PDF_1MB.pdf")

# 5) Convert the pdf into document objects 

pages = loader.load()

#6) printing the pages/chunks 

#7) 
print(f"\n------Page Content-------")
print(pages[0].page_content)

print(f"\n-----Metadata------")
print(pages[0].metadata)
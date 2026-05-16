import instructor
from google import genai 
from pydantic import BaseModel, Field 
import os 

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)
if not gemini_api_key:
    raise ValueError("API key is missing. Please use correct gemini api key")

corporate_text = """
MEMO RE: Q4 Scaling
Date: Oct 12, 2026
Written by: Jaymin
We need more cloud budget for the 'Extract Once, Judge Many' pipeline. 
The architecture is bottlenecking. Tony and Marten will lead the review.
"""

print("==== Starting prompt engineering pipeline=====")
print("1. ZERO SHOT PROMPTING")
zero_shot_prompt = f"Extract the author from this text: {corporate_text}"

response_zero = client.models.generate_content(
    model='gemini-2.5-flash', contents=zero_shot_prompt
)
print(response_zero.text)
print("-"* 40)
print("2. FEW-SHOT OUTPUT")

few_shot_prompt = f"""
Extract the author from the text. Respond ONLY with the name. 
Example 1 input: "Memo: Server down. Written by Tony." --> Example 1 output: Tony
Example 2 Input: "Update from Marten regarding sales." -> Example 2 Output: Marten

Real Input : {corporate_text}

"""

response_few = client.models.generate_content(
    model='gemini-2.5-flash', contents=few_shot_prompt
)

print(response_few.text)
print("-"* 40)

print("3. Chain of Thought Output:")
cot_prompt = f"""
Analyze the following text to find the primary author. 
Think step by step. First, identify any names in the text. Second look 
for keywords like "Written by" or "From" near those names. Third, declare the author.

Text: {corporate_text}
"""
response_cot = client.models.generate_content(
    model='gemini-2.5-flash', contents=cot_prompt
)

print(response_cot.text)
print("-"* 40)

class DocumentMetadata(BaseModel):
    title: str = Field(description="The official title of the document.")
    author: str = Field(description="The name of the employee who wrote it. Use 'UNKNOWN' if missing")
    summary: str = Field(description="A strict 1-sentence summary of the content.")

instructor_client = instructor.from_genai(
    client=client,
    mode=instructor.Mode.GENAI_STRUCTURED_OUTPUTS
)

mega_prompt = f"""
You are an expert corporate data extraction algorithm. 
CONTEXT: Processing raw text extracted from corporate PDFs.
TASK: Extract the official title, the author, and a 1-sentence summary based on the provided schema. 
RULES: Do not guess. If data is missing, follow the schema instructions exactly.

REAL INPUT: 
{corporate_text}
"""

extracted_data = instructor_client.chat.completions.create(
    model="gemini-2.5-flash", 
    messages=[{
        "role": "user",
        "content": mega_prompt
    }],
    response_model=DocumentMetadata
)

print(extracted_data.model_dump_json(indent=2))
print("\n[System] Successfully extracted author directly into Python variable:", extracted_data.author)

print("=====PIPELINE COMPLETE=======")
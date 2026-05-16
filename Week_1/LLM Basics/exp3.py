# to do 
# text = """
# Invoice from Aamzon
# Date : 12 Jun 2025
# Total : 1200
# """

#pass this messy text and ask LLM to convert it into structured Json format 

from google import genai 
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_api_key)

text = """
Invoice from Aamzon
Date : 12 Jun 2025
Total : 1200
"""

def extract_invoice_date(api_key = gemini_api_key):
    prompt = f"""

        Extract the following from this invoice:
        -total amount 
        -date 
        -vendor_name
        Return the output in JSON only.

        Invoice : {text}
    """

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents = prompt
    )

    return response.text

print(extract_invoice_date(text))

# to do 
""" Ask the agent to explain gravity
Generic prompt : "What is gravity?"
Role 1 : Act as a kindergarten teacher
Role 2: Act as quantum phycisist
"""
from google import genai 
import os 

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = gemini_api_key)
if not gemini_api_key:
    raise ValueError("API key is missing. Please use correct gemini api key")

# prompt = f"Check logs : {logs}" -- > #bad prompt
prompt1  = """ What is gravity?"""

prompt2 = """Act as a kindergarten teacher and explain What is gravity"""

prompt3 = """Act as a quantum phycisist and explain What is gravity"""



response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt3
)

print(response.text)
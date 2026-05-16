from google import genai 
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_api_key)

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = "What is AI?"
)

print(response.text)
from google import genai 
import os 

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = gemini_api_key)
if not gemini_api_key:
    raise ValueError("API key is missing. Please use correct gemini api key")

# prompt = f"Check logs : {logs}" -- > #bad prompt

# Zero Shot prompt
prompt1  = """Classify this review as Positive or Negative: 'The UI is incredibly clunky."""

#Single Shot prompt
prompt2  = """Classify reviews as Positive or Negative. 
            Example Input: 'I love the new layout'--> Example Output: Positive

            Review : 
            """

review = "The UI is incredibly clunky"


response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt2 + review
)

print(response.text)
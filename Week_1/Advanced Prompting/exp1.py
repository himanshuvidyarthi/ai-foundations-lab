# logs analyzer for errors

from google import genai 
import os 

gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key = gemini_api_key)
if not gemini_api_key:
    raise ValueError("API key is missing. Please use correct gemini api key")

logs = f"""
    Logs:
        [INFO] Server Started
        [INFO] SQL Database Connected 
        [INFO] Mongo Databse Connected 
        [ERROR] Redis DB Connection failed 
        [INFO] WOHqHQOIS;H user landed on dashboard 
        [INFO] WOHqHQOIS;H landed on checkout
 """

# prompt = f"Check logs : {logs}" -- > #bad prompt
prompt  = f"""
    You are a Devops engineer. 
    Analyze the logs and identify ERROR issues only. 
    Return only error messages.

    Logs: {logs}
"""

response = client.models.generate_content(
    model = "gemini-2.5-flash",
    contents = prompt
)

print(response.text)
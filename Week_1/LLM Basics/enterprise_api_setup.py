import time 
import random 
from google import genai 
from google.genai import types 
import os 

model_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = model_api_key)

def generate_with_backoff(prompt_text, max_retries=5):
    for attempt in range(max_retries):
        try:
            start_time = time.time()

            response = client.models.generate_content(
                model = "gemini-2.5-flash",
                contents = prompt_text,
                config = types.GenerateContentConfig(
                    temperature= 0.7, 
                    top_p = 0.9
                )
            )

            end_time = time.time()
            duration = end_time - start_time # latency

            return response.text, duration
        
        except Exception as e:
            print(f"[Warning] Attempt {attempt + 1} failed. Error: {e}")

            if attempt == max_retries -1:
                print("Max retries reached. Server is unresponsive")

            sleep_time = (2 ** attempt) + random.uniform(0,1)
            print(f"Waiting {sleep_time: .2f} seconds before retrying...")
            time.sleep(sleep_time)

my_prompt = """
Write a short, professional, but slightly humorous welcome message 
for my team members Marten, Tony, and Jaymin, who are joining me on 
the new 'Extract Once, Judge Many' pipeline project today.
"""

print("sending request to Google servers.. \n")

result_text, time_taken = generate_with_backoff(my_prompt)

print("---AI Response---")
print(result_text)
print("-"* 10)
print(f"\n [Metrics] Requests completed in {time_taken: .2f} seconds.")

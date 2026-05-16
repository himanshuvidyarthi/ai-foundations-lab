from google import genai 
import os
gemini_api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key = gemini_api_key)

def generate_multi_context(topic):
    prompts = {
        "tweet": f"Write a short tweet about {topic}",
        "Linkedin" : f"Write a short professional Linkedin post about the {topic}",
        "email": f"Write a short email about the {topic}"
    }

    results = {}

    for key, prompt in prompts.items():
        response = client.models.generate_content(
            model = "gemini-2.5-flash",
            contents = prompt
        )

        results[key] = response.text
    
    return results 

output = generate_multi_context("AI in healthcare")

for k,v in output.items():
    print(f"\n-------- {k.upper()}--------\n{v}")


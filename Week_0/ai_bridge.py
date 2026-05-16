from pydantic import BaseModel, ValidationError 
import requests 

class UserInsight(BaseModel):
    user_name: str 
    sentiment_score: int 
    is_flagged: bool 

# def analyze_user_data_via_api():
#     try: 
#         api_url = 'https://jsonplaceholder.typicode.com/posts' #mock-api
#         headers = {
#             "Content-Type" : "application/json",
#             "Authorization": "Bearer mock api key" #internal token
#         }

#         payload = {
#             "model": "gpt-4o",
#             "message": [
#                 {"role": "user", "content": "Analyze sentiment"},
#                 {"role": "sytem", "content": "Analyze Alice"}
#             ]
#         }
        
#         reponse = requests.post(api_url, headers = headers, json = payload, timeout = 5)

#         print(reponse.json())

#     except: 
#         print("Something went wrong!")

# analyze_user_data_via_api()

def analyze_user_data_via_api():
    try: 
        api_url = 'https://jsonplaceholder.typicode.com/posts' #mock-api
        headers = {
            "Content-Type" : "application/json",
            "Authorization": "Bearer mock api key" #internal token
        }

        payload = {
            "model": "gpt-4o",
            "message": [
                {"role": "user", "content": "Analyze sentiment"},
                {"role": "sytem", "content": "Analyze Alice"}
            ]
        }
        
        reponse = requests.post(api_url, headers = headers, json = payload, timeout = 5)

        mock_llm_output = {
            "user_name": "Alice",
            "sentiment_score": "-28", 
            "is_flagged": "True"
        }

        validated = UserInsight(**mock_llm_output)
        print(validated)
        print(validated.sentiment_score + 10)

        print(type(validated.sentiment_score))
        print(type(validated.is_flagged))
    
    except ValidationError as e:
        print(e.json())

analyze_user_data_via_api()



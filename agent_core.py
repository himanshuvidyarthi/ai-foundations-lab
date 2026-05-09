# from dataclasses import dataclass, asdict 
import json 

# @dataclass 
# class AgentProfile: 
#     agent_name: str 
#     model_engine : str 
#     max_retries : int = 3 
#     is_active : bool = True 

# primary_agent = AgentProfile(  # instance of the class
# agent_name = "Databot_v2",
# model_engine = "gpt-4-turbo"
#     )
 
# print(f"Agent: '{primary_agent.agent_name}' initialized on {primary_agent.model_engine}" )

# #sale parsing of the data files 

# config_filename = "agent_config.json"

# print(f"\n------saving configuration-------")
# with open(config_filename ,"w") as file:
#     json.dump(asdict(primary_agent), file, indent = 4)

# print(f"Configuration securely saved to {config_filename}")


## Mock API Call ###
import time 
def mock_api_call(payload: dict, simulate_timeout = False, simulate_missing_key = False):
    print(f"\n ---- Initiating API call----")

    try: 
        if simulate_missing_key: 
            malformed_message = {
                "text": "Hello, World"
            }
            tokens = malformed_message["usage_metrics"]

        if simulate_timeout:
            time.sleep(1)
            raise TimeoutError("The LLM API endpoint took too long to respond.")
        
        print("API call successful")
        return True 
    except KeyError as e: 
        print(f"[CRITICAL ERROR] LLM output parsing failed. Missing expected key: {e}")

    except TimeoutError as e: 
        print(f"[NETWORK ERROR] {e} Switching to backup endpoint...")

    finally: 
        print("API transaction finalized (Connection Closed!)")

if __name__ =="__main__":
    #test 1
    # mock_api_call(payload = {"data" : "test"}, simulate_missing_key= True)
    #test 2 
    mock_api_call(payload = {"data" : "test"}, simulate_timeout= True)
    
# Exercise 

# user_dict --> (name, age, gender, email)
# store this inside a file "user.json" in json format

user = {
    "name": "Alice",
    "age": 20, 
    "gender": "Female",
    "email": "aliceinwonderland@gmail.com"
}

# dumping json data
with open("user.json", "w") as file:
    json.dump(user,file, indent = 4)

#reading json file
with open("user.json", "r") as file:
    data = json.load(file)

print(data)


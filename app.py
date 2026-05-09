name = ["Alice", "Bob", "Charlie"]

user = {
    "name": "Alice",
    "age" : 25
}

user_database = [
    {"id": 101, "name" : "Alice", "role": "admin", "is_active": True},
    {"id": 102, "name" : "Bob", "role": "user", "is_active": False},
    {"id": 103, "name" : "Charlie", "role": "editor", "is_active": True},
]

print(user_database)

#Traditional approach 
active_users = []
for user in user_database:
    if user["is_active"]: 
        active_users.append(user["name"])
print(active_users)

# Actual approach 
active_users = [user["name"] for user in user_database if user["is_active"]]
print(active_users)

print(f"System log: Found {len(active_users)} active_users.\n")

#range based iteration 

for i in range(len(name)):
    print(name[i])

salaries = [30000, 40000, 50000]
for i in range(len(salaries)):
    salaries[i] += 5000

print(salaries)

#gives you access to just read only values
for i in name:
    print(i)


#enumerate -- to get the value and index at the same time for every iteration 
for index, _name in enumerate(name):
    print(f"{index}, {_name}")

#zip -- it helps iterates 2 lists parallely 
students = {'Alice', "Bob", "Charlie"}
scores = [85, 98]

for student, score in zip(students, scores):
    print(f"{student} scored {score}")

for key in user:
    print(key)


for value in user.items():
    print(value)

for key, value in user.items():
    print(f"{key}- {value}")

matrix = [
[1,2,3],
[4,5,6],
[7,8,9]
]

for row in matrix: 
    for value in row:
        print(value)

#it is used to catch any unexpected API parameters
# def demo(**kwargs): #it helps in dynamic list of params
#     print(kwargs)


# demo(a=1)

# demo(a=1, b=2, c =3)


# print the key, value pairs for each user 

def print_all(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")
        print("======End=====")


print_all(name = "Alice")
print_all(name = "Alice", age = 25)
print_all(name = "Alice", age = 25, role = "admin")


def config(**kwargs):
    temp = kwargs.get("temperature", 0.5)
    print(temp)

config()

# Kwargs helps in future proofing which means if models have different params it will get invoked

context_block = "" 
for index, name in enumerate(active_users, start = 1):
    context_block += f"{index}. {name}\n"

system_prompt = f"""
    System instruction : You are a corporate communication assistant. 
    Task: Write a highly professional welcome message for the following active member.

    Active Members:
    {context_block}

    Please keep the tone encouraging and brief. 
    """

print("------GENERATED PROMPT/PAYLOAD-----")
print(system_prompt)

def execute_mock_llm_call(prompt_text, model_engine = "gpt-4", **kwargs):
    print(f"Routing request to target_model: {model_engine}")

    print(f"Applying dynamic configuration {kwargs}")

    print(f"Awaiting API response \n")

    return f"Mock API output: Welcome aboard, {', '.join(active_users)}! Let's get to work."

if __name__ == "__main__":
    api_response = execute_mock_llm_call(
        prompt_text= system_prompt,
        model_engine= "gpt-4-turbo",
        max_tokens = 250,
        top_k = 250
    )

    print(f"Final Result: \n{api_response}")

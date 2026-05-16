# https://jsonplaceholder.typicode.com/posts/1

import requests 

# get api call 

response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

print(response.status_code)
print(response.json())


# post api call
url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Hello title", 
    "body" : "Trying to test the api", 
    "userId":1 
}

response = requests.post(url, json = data)
print(response.status_code)
print(response.json())
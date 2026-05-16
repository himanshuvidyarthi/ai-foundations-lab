data = {
    "score": 90, 
    "flag": False
}

print(data["score"] + 10)


# def process_score(score: int)-> int :
#     print("Line 10 ->", score)
#     return score + 10 

# rs = process_score("10")


def greet(name:str)-> str:
    return "Hello " + name 

print(greet(10))
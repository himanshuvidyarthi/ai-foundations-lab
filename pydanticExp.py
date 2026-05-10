from pydantic import BaseModel 

# 1) Basemodel allows us to specify the data keys and there corresponding type
# 2) Performs auto type casting 

# class User(BaseModel):
#     name: str 
#     age: int 

# data = {
#     "name": "Alice",
#     "age": "30"
# }

# user1 = User(**data)

# print(user1) 
# print(type(user1.age)) 


#to do 
#basemodel class structure -> product -> (name, price, in_stock)
#create an instance of it ("abcd", "2000", "False")

class Product(BaseModel):
    name: str
    price: float
    in_stock: bool 

product1 = {
    "name" : "Laptop",
    "price" : "55000",
    "in_stock" : "0"
}

p1 = Product(**product1) 

print(type(p1.price))
print(type(p1.in_stock))
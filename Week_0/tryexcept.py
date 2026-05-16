# num = int(input("Enter a number: "))
# result = 10/num 
# print(result)


# try: 
#     num = int(input("Enter a number: "))
#     result = 10/num 
#     print(result)

# except ZeroDivisionError:
#     print("You cannot divide by zero")

# except ValueError as e: 
#     print("Please enter a valid number.", e)

# except: 
#     print("Error Occured!")

# else: 
#     print(f"Success! The result is {result}")

# finally:
#     print("Division attempt finished. Cleaning up resources.")

# try:
#     file = open("data.txt", "r")
#     content = file.read()

# except FileNotFoundError:
#     print(" File not found!")

# try: 
#     num = int(input("Enter a number: "))
#     result = 10/num 
#     print(result)

# except(ZeroDivisionError, ValueError):
#     print("Given value is not valid for division")


try: 
    lst = [1,2,3]
    print(lst[3])
except IndexError:
    print("Invalid index to access the value!")


# try:
#     #risky code 

# except:
#     #handle error

# finally:
#     #always run
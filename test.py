#zip -- it helps iterates 2 lists parallely 

from itertools import zip_longest
students = {'Alice', "Bob", "Charlie"}
scores = [85, 98]

for student, score in zip(students, scores):
    print(f"{student} scored {score}")



for student, score in zip_longest(students, scores, fillvalue = "Missing"):
    print(f"{student} scored {score}")



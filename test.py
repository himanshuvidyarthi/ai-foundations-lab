#zip -- It takes multiple iterables (like lists or tuples) and "zips" their corresponding elements together into pairs.

from itertools import zip_longest
students = {'Alice', "Bob", "Charlie"}
scores = [85, 98]

for student, score in zip(students, scores):
    print(f"{student} scored {score}")



for student, score in zip_longest(students, scores, fillvalue = "Missing"):
    print(f"{student} scored {score}")



"""
Zip:
Easily combine 2 list

In order to see the content of a zip it must be casted to a list

if different lengths, the result will be the shortest list
"""

name = ["Marko", "Thomas","Frank","Imma"]
surname = ["Võsa","Putah","Lola","McDonald's"]
age= [28, 30, 20, 18]

print(list(zip(name, surname, age)))

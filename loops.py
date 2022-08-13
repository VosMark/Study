"""
While loop:
Executes a set of sentence  until the condition is no longer valid
"""
i = 10
while i > 3:
    print(i)
    i -= 2 # i = i -1

"""
break:
stops the loop even if the condition is valid
"""
i = 10
while i > 3:
    print(i)
    if i == 6:
        break
    i -= 2

for x in range(i):
    if x == 6:
        continue
    print(x)
#Tra no ajab jooma
"""
Continue: stop the current iteration and advances to the next
"""

name = input("What is your name")
print(f"My name is {name}")
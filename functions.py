"""
A function is a block of code/sentences that runs only when it is called
- can have parameters, i.e it can accept input
- it can return a result

def <<function_name>>(): # a function without parameters and does not return a value/result
    sentences

def <<function_name>>(): # a function without parameters and returns a value/result
    sentences
    return <<data>>
"""

def print_name():
    name = input("Your name")
    print(f"What a nice name {name}!!")

#call a function by its name
#print_name()

def return_name():
    name = input("Your name")
    return name

#fname = return_name()
#print(f"You have a lovely name {fname}")

"""
arguments are information passed into a function
def <<function_name>>(<<argument>>, ......, <<arguments>>): 
    sentences
    return <<data>>

"""

def my_name(name, age):
    print(f"You have a lovely name {name} for your age {age}")

# my_name("Oyin", 10)
# my_name(10, "Oyin")
# my_name(age = 10, name="Oyindolapo") # named arguments

#calling your function
# func_name(<<name_param>> = value)
def area_of_square(length):
    return  length ** 2

def area_of_rectangle(len, breath):
    return  len * breath

def get_shape(len=3, breadth=5):
    if len == breadth:
        area = area_of_square(length=len)
        print(f"Shape is a square with area {area}")
    else:
        print(f"Shape is a rectangle with area {area_of_rectangle(len, breadth)}")

get_shape(len=10, breadth=8)
get_shape()

"""
You can have default values for your functions, such that, if no arguments is passed, 
the default value is used
"""

def isogram(word):
    l = [x for x in word.lower()]
    if len(set(l)) == len(l):
        return True
    else:
        return False

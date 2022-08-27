"""
python
    -create a function inside another function
    -pass a function as an argument to another function
    -a function can return another function
A decorator is a function that takes another function and
extends the behaviour of the latter function without explicitly modifying it
"""

def increment_num(num):
    return num + 2

print(increment_num(3))

"""Using a function as an argument"""

def welcome_student(name):
    return f"Welcome {name} from the break"

def did_you_study(name):
    return f"I hope you studied and revised python {name}"

def greetings(any_func):
    return any_func("Marko")

print(greetings(did_you_study))
print (greetings(welcome_student))

"""
Create a function inside another function - nested function
-Inner function s are not defined until the parent function is called/executed
-Inner function is local to your function, hence they are not available outside the parent
"""

def outer_box():
    print("This is a parent box")

    def middle_box(): #inner function
        print("This is the middle box")
    def last_box(): #inner function
        print("This is the last one". upper())

    middle_box()
    last_box()
outer_box()

"""
function returning another function
"""
def greeting(hour):
    def morning(name):
        return f"Good morning {name}"

    def afternoon(name):
        return f"Good afternoon {name}"

    def evening(name):
        return f"Good evening {name}"

    def night(name):
        return f"Good night {name}"

    if hour < 12: # between 0-11
        return morning
    elif hour >= 12 and hour <= 17:
        return afternoon
    elif hour >=17 and hour < 20:
        return evening
    else:
        return night

greet = greeting(14)
print(greet("Marko"))

"""
Decorator
 - Takes a function as an argument
 - Defines an inner function
 - Returns the function as the result of its operation
 
"""

def my_decorator(func):
    def wrapper():
        print(f"This is my wrapper")
        func()
    return wrapper

def say_cheese():
    print("Python is fun!")

my_decorator(say_cheese)()

@my_decorator
def say_something():
    print("Saying something")

say_something()

def increment(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@increment
def just_a_num(num):
    return num + 3
@increment
def two_nums(num1, num2):
    return num1+3, num2+3

print(just_a_num(5))
print(two_nums(10, 8))

"""
a, b, c = (10, 3, 6) : *args == positional arguments
**kwargs == named arguments
num3 = 3, num2 = 10, num3 = 6

positional comes before named
"""
def some_example(**kwargs):
    for x in kwargs.values():
        print(x)
    print("Doing something")

#some_example(10, 3, 7) #Positional
#some_example(2,3,4,5,6,7)
some_example(val2= 10, val3= 6, val1= 8) #Named arguments
#some_example(8, 7, val3=17)
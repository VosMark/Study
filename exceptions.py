"""
Error terminates the Python code being executed
- Syntax error/parser error
    - shows the error with ^
    - most IDE catches this error
- Exceptions: errors that occur during execution
    - code is syntactically correct
    - but error when you try to execute your code

Exception handling:
Try: block of code that might generate error/ run this code
Except: Handle the exception
Else: Execute a code when there is no error
Finally: Finally executes whether an error occurs or not
"""
try:
    print(10/2)
except:
    print("Do nothing")
else:
    print("No error occured")
finally:
    print("I occur regardless of an error")

try:
    x = 10
    y = [10, 2, 3, 0, 4, 6]
    z = [x/m for m in y]
except:
    print("Ran into an error")
finally:
    print("I occur regardless of an error")
          
"""Example: Database connection
try: make a connection
except: error
finally: close the connection
    
read and write to a file
try: read the file
    write to a file
except: error that occurs during the reading of the file
else: close the file
"""


"""
Types of Exceptions
- Arithmetic error: ZeroDivisionError eg 10/0
                    Overflow error
- Assertion error: When assertion fails
- EOF error
- Input error
- ModelNotFound error
- Index error
- Key error
- Name error
"""

"""Multiple Exceptions"""

try:
    print(name)
except NameError as err: #Named exceptions
    msg = err
    print(f"a new message: {err}")
except:
    print("Other errors")

"""Creating customized Exceptions"""
class NoNegativeInList(Exception):
    pass

"""Raise exceptions"""
list1 = [10, 4, 5, 6, -1, 7, 7]

for x in list1:
    if x < 0:
        raise NoNegativeInList("Negative values shouldn't be in the list")


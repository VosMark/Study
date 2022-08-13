"""
Tuples:
    - ordered
    - unchangeable
    - created/denoted with ()
    - allow duplicates
"""

tuple1 = ('oranges',) # put a comma after a tuple with 1 item
print(type(tuple1))

"""
Add items : convert tuple to a list, append the item and convert back to tuple
"""

x= list(tuple1)
x.append('lemon')
tuple1 = tuple(x)
print(tuple1)

tuple2 = ('star fruit',)
tuple1 += tuple2
print(tuple1)

"""
Unpacking of tuple

The number of items in your tuple should be equal to the len of the tuple

if not, you can use * to unpack the remaining to a list
"""
fruit1, fruit2, fruit3 = tuple1
print(fruit2)

fruit, *fruit_2 = tuple1
print(fruit_2)
print(type(fruit_2))
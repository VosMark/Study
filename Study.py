mylist = ['apples', 'mangoes', 2, 7.5, 'red', 'apples', 2]
print (type(mylist))
print (mylist[0])
print(mylist[-1])
print(mylist[2:4])
# Use in to check if a value exists in a list
print('guava' in mylist)

"""
Add items to a list
- append: adds to the end of a the list
- insert: adds at a specific index
    <<list>>.insert(<<position>>, value)
- extend> appends elements from a list to another list
    <<current_list>>.extend(<<new_append_list>>)
"""
mylist.append('guavas')
mylist.append('grapes')
mylist.insert(2, 'blueberries')
mylist.insert(0, 'mangoes')
print(mylist)

exotic_fruits = ['cashew', 'wild blueberries', 'passion fruit']

mylist.extend(exotic_fruits)


mylist[4] = 'corn'
print(mylist)

"""
remove items in a list:
    -remove: <<list>>.remove(<<item>>)
        -with duplicate instances, the first is removed
    -pop: removes the last item <<list>>.pop()
    <<list>>.pop(<<index>>): removes item at the position
    -clear: removes all the items in a list
"""
mylist.remove(7.5)
mylist.remove(2)
mylist.pop()
print(mylist)
mylist.pop(1)
print(mylist)
exotic_fruits.clear()
print(exotic_fruits)

age = [12, 14, 25, 39, 67, 45, 13]
print(min(age))
print(max(age))
print(sum(age))
print(sum(age) / len(age))

mylist.sort()
age.sort()
print(mylist)
print(age)

mylist.reverse()
print(mylist)

"""
Looping through a list
-for loop
    for <<variable>> in <<list>>:
    statements
"""
ages = 10
name = 'Marko'
print (f'My name is {name}, I am {ages} years old')
print('My name is {} and I am {} years old'.format(name, ages))

for var in mylist:
    print(f'I love {var}')
    print('I love ' + var)
    print('I love {}'. format(var))

for item in age:
        print(item/2)

"""
range(start, stop, step

default step is 1
"""

for i in range(len(age)):
    print(f"index {i}: {age[i]}")

"""
List comprehension:
    -creates a new list
    -short method of creating a list from a existing list
    -filter and perform operations
    
    [<<expression>> for <<variable_name>> in <<list>> <<optional :condition>>]
"""
x= [print(f"my age is {x}") for x in age]

new_age = [x for x in age if x%2 == 0]
print(new_age)

upp_list = [var.upper() for var in mylist]
print(upp_list)

"""

Set:

    - a collection
    - unordered
    -unchangeable
    -unindexed, you cannot access then through index
    -created/denoted with {}
    -set do not allow duplicates
"""

myset = {'mangoes', 'guaves', 'berries', 'honeydew', 'mangoes'}
print(myset)
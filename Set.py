"""
Set
- a collection
    - unordered
    -unchangeable
    -unindexed, you cannot access then through index
    -created/denoted with {}
    -set do not allow duplicates
"""

myset = {'mangoes', 'guaves', 'berries', 'honeydew', 'mangoes'}
print(myset)
print(len(myset))

for x in myset:
    print(x)

print('honeydew' in myset)

"""
Add items ti a set:
    - add <<set>>.add(<<item>>)
    - update - adds item from a set into another set
    <<set1>>.update(<<set2>>)
    - add any iterable/collection to a set
"""

myset.add('canteloupe')
print(myset)

nuts = {'cashew', 'peanut', 'almonds', 'guavas'}
myset.update(nuts)
print(myset)

citrus = ['oranges', 'tangerine', 'lemon', 'lime']
myset.update(citrus)
print(myset)

"""
Removing elements from a set:
    -remove<<set>>.remove(<<item>) this generates an error if the item doesn't exist
    -pop: removes the last item in the set, 
    but remember that a set is unordered, thus you have no idea/control over what's getting removed
    -discard: this doesn't return error if item isn't found
    -clear
"""
myset.remove('guavas')
print(myset)
myset.discard('passionfruits')
myset.pop()
print(myset)

"""
Joining of set:
    - union: create a new set with items from the 2 sets.
Union also removes duplicates if it occurs
"""
set1= {'peanut', 'oranges', 'berries', 'almonds', 'cantaloupe'}
set2= {'cantaloupe', 'mangoes', 'honeydew', 'lime', 'tangerine', 'lemon'}

set3 = set1.union(set2)
print(set3)

"""
To get common values(duplicates) within a set:
    -intersection <<set1>>.intersection(<<set2>>)
    -intersection_update = what is common to both
"""
set1.intersection_update(set2)
print(set1)
print(set2)
set3.symmetric_difference_update(set2)
print(set3)

print(set3.isdisjoint(set2))
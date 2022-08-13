"""
key:value pair
it is ordered
it is changeable
keys do not allow duplicates
<<dict_name>> = {
<<key>>: <<value>>,
<<key>>: <<value>>
}
"""

std = {
    "name": "Marko",
    "age": 23,
    "occupation": "Master engineer"
}

"""
Access Items in a dict:
-using keys as a index
- use get method, returns
"""
print(std["age"])

"""
get all keys
-keys method returns a list of all the keys in a dict
<<dict>>.keys()
"""
print(std.keys())

"""
add items to a dict
-use key_value pair
    <<dict>[<<new_key>>] = <<value>>
    -update()
    <<dict>>.update({
                    <<key>>:<<value>>
                    })

"""

std["is_student"] = "no"
std["name"] = "Marko"
print(std)

std.update(
    {
        "best_color": "black"
    }
)
print(std)

new_dict = {
    "height" : 183,
    "weight" : 80,
    "hair_color" : "blonde"
}
std.update(new_dict)
print(std)
#std.update({height}: 183))
"""
Remove items in a dictionary: 
- pop : generates error if key doesn't exist
<<dict>>.pop(<<key>>)
- popitem() : removes the last item in the dict
- clear() : empties your dictionary
"""
std.pop("height")
std.popitem()
print(std)

"""
Loop through a dict:
.values() : returns the values in the dict  
"""
for item in std: #returns the key or use <dict>.keys()
    print(item, std[item])

for val in std.values(): # returns dict values
    print(val)

for key, val in std.items(): # returns key and values
    print(f"{key}:{val}")

# dictionary comprehension
print({k: str(v).upper() for k,v in std.items()})

"""nested dictionary
<<dict>> = {
<<keys>>: {
            <<key>>:<<value>>
            ....
            <<key>>:<<value>>
        },
<<keys>>: {
            <<key>>:<<value>>
            ....
            <<key>>:<<value>>
        }
...
}
"""
students = {
        "Marko" : {
            "is_std" : False,
            "age" : 23
        },
        "Thomas":
            {
                "is_std": True,
                "age": 20
            },
        "Frank":{
            "is_std": True,
            "age": 30,
            "hair_color": "red"
        }
}
print(students.keys())
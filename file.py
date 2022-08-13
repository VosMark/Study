import os
"""
File Operations:
- Creating
- Reading
- Updating
- Deleting

open(<<filename>>, <<mode>>)
r = read => default opens the file for reading, error if file doesn't exits
w = write - open the file for writing, creates the file if not exist
a = append - open the file for appending, if file not exist, creates the file
x = create - create the new file, error if file exists

t = text mode => default
b = binary
"""
# Read a file
if os.path.exists("test.txt"):
    f = open("test.txt")
    print(f.read())
    f.close()

    f = open("test.txt", "a")
    f.write("\nOhhh, It's going to rain. \nThe beautiful day isn't for outdoor activities")
    f.close()

with open("test.txt","a") as f:
    f.write("\nI won't be able to cycle. \nI think I will paint")

if os.path.exists("test.txt"):
    os.remove("test.txt")
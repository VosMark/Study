#Given 2 strings, can you make fist string from the second by deleting some characters s1 = "Hello" s2= "vufigsaHudesdflelio"

def canMakeStr2(s1, s2):

    count = {s1[i]: 0 for i in range(len(s1))}

    for i in range(len(s1)):
        count[s1[i]] += 1

    for i in range(len(s2)):
        if (count.get(s2[i]) == None or count[s2[i]] == 0):
            return False
        count[s2[i]] -= 1
    return True


# Driver Code
s1 = "vufigsaHudesdflelio"
s2 = "Hello"

if canMakeStr2(s1, s2):
    print("Yes")
else:
    print("No")

#Sum numbers until flag -9999 is seen [10, 23.4, 67, -9999, 7, 8, 100]
list1 = [4,45,69,8,2,3,5,6 ,-9999,12,8,9]
def sum_number(nums:list) -> float:
    sum = 0
    for x in nums:
        if x != -9999:
            sum += x
        else:
            break
    return sum
sum_number(list1)

#Find the min and max of set of numbers

sets = set([8, 16, 24, 1, 25, 3, 10, 65, 55])
def MAX(sets):
    return (max(sets))
def MIN(sets):
    return (min(sets))
print((MAX(sets), (MIN(sets))))
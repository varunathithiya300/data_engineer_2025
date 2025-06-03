# 1. Creating a list
list_1 = [1, "Asd", 45]
list_2 = list((1, "Asd", 45))
# print(list_2)

# 2 . Adding elements to a list
# .append()
# .extend()
# .insert(index, element)

# 3. Updating element
# list[index] = value

# 4. Removing elements in a list
# .pop(element) - removes the first occurance of the element
# .remove(index)
# del list[index] - 

a = [1, 2, 2, 3, 4, 55, 55, 55]
# print(list(dict.fromkeys(a)))

# Ways to deduplicate a list
# 1. b = set(a)
# 2. using list comprehension
def deduplicateList(a):
    res = [] # initiate an empty list
    for val in a:
        if val not in res:
            res.append(val)
    print(res)
# deduplicateList([1, 2, 2, 3, 4, 55, 55, 55])

# 3. dict.fromkeys()
# print(list(dict.fromkeys([1, 2, 2, 3, 4, 55, 55, 55])))

# Reverse a list
# .reverse() -> inplace reverse
# reversed(list) -> returns an iterator. Convert the result to a list.
# using for loop - > 
    # initiate an empty list. Loop the input list and insert every element at zeroth index
# list slicing -> list[::-1]

def reverseList(a):
    result = []
    for i in a:
        result.insert(0, i)
    print(result)
reverseList([1, 2, 2, 3, 4, 55, 55, 55])
b = [2, 3, 4]
b.reverse()
print(b)
print(list(reversed(a)))
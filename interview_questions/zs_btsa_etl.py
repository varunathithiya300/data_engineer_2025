""" 
Role - Business Technology Solutions Associate - ETL Developer

Concepts covered
    1. Creating a dictionary out of two lists of equal length
    2. Sorting the above dictionary based on the value in descending order

"""

l1 = ['a', 'b', 'c']
l2 = [1, 2, 3]

d1 = {k:v for k,v in zip(l1, l2)}
# print(d1)


# Creating a dictionary without using zip
# This approach will work if the length of both the lists are equal

d2 = dict()
for i in range(len(l1)):
    d2[l1[i]] = l2[i]
# print(d2)

# If the length of the lists are different
# Case 1 - length of key list > length of value list - A dictionary with available keys is created
l3 = ["a", "b"]
l4 = [1, 2, 3]
d3 = dict()
for i in range(len(l3)):
    d3[l3[i]] = l4[i]
# print(d3)

# Case 2 - length of key list < length of value list -> Index error
l5 = ["a", "b", "c"]
l6 = [1, 2]
d4 = dict()
for i in range(len(l5)):
    d4[l5[i]] = l4[i]
# print(d4)

# Approach to fill with a default string
for i in range(len(l5)):
    if i < len(l6):
        d4[l5[i]] = l6[i]
    else:
        d4[l5[i]] = "na"
# print(d4)

# Sorting a dictionary based on its values
# sorted() returns a list


d5 = dict(sorted(d1.items(), key = lambda item: item[1], reverse = True))
print(d5)
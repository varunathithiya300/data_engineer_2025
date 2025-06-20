
import numpy as np

# arr.shape = to find the shape of the array
# arr.dtype = to find the data type of the array

arr = np.array([1, 3, 3, 3, 4, 4, 5, 7, -9])

# Understanding the differences between a list and an array
a = [1, 2, 3]
b = [4, 5, 6]
c = []
d = np.array(a) + np.array(b)
for i in range(len(a)):
    c.append(a[i] + b[i])

# Count the number of time a value occurs in an array.
# np.bincount(arr) -> max(arr) -> range(0, max(arr)+1)

arr_2 = np.array([2, 3, 4, 4, 6, 6, 6, 1])


# np.where(condition)
# np.nonzero

# result = np.where(arr_2 >= 4)[0]
# print(result)
# print(arr_2[result])

arr_3 = np.array([5, 6, 7, 8, 9])
result_2 = np.where(arr_3%2 == 0)[0]

# Testing np.where for a 3D array
arr_4 = np.array([
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ],
    [
        [13, 14, 15, 16],
        [17, 18, 19, 20],
        [21, 22, 23, 24]
    ]
])


# Constructing a 3D array

arr_3d = np.array([
                    [[1, 2], [3, 4]], 
                    [[4, 5], [6, 7]], 
                    [[7, 8], [9, 10]]
                ])

print(f"Shape of arr_3d is {arr_3d.shape}")
print(f"Number of dimensions in arr_3d is {arr_3d.ndim}")

arr_3d_2 = np.array([
    [
        [1, 2, 3, 4],
        [1, 2, 3, 4],
        [1, 2, 3, 4]
    ],
    [
        [5, 6, 7, 8],
        [5, 6, 7, 8],
        [5, 6, 7, 8]
    ],
    [
        [5, 5, 5, 5],
        [5, 5, 5, 5],
        [5, 5, 5, 5]
    ]
])

# 2x3x4
# 3x3x4
print(arr_3d_2.shape)
print(arr_3d_2.ndim)

arr5 = np.array([[1, 2], [3, 3]])
print(arr5)
arr5 = np.delete(arr5, obj=0, axis=1)
new_insert = [5, 9]
arr5 = np.insert(arr5, obj=0,values=new_insert, axis=1)
print(arr5)
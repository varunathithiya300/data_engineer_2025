import numpy as np
from typing import List, Union

""" 
To generate an array of numericals using numpy

1. np.array(list of numbers) -> manually pass a list
2. np.arange(start, stop, step) -> For evenly spaced values
3. np.linspace(start, stop, num) -> For evenly spaced values including stop
4. np.random.randint(low, high, size) -> Random integers
5. np.random.rand(n) or np.random.randn(n) -> Random floats

"""

def generateArray(start: int, stop: int, num: int) -> List[float]:
    arr = np.linspace(start, stop, num)
    np.random.shuffle(arr)
    return arr.tolist()

def bubbleSort(start: int, stop: int, num: int) -> List[float]:
    arr = generateArray(start, stop, num)
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
    
print(bubbleSort(4, 21, 5))
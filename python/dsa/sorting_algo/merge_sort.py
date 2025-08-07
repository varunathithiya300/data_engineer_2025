def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i+1
        else:
            result.append(right[j])
            j = j+1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(merge_sort([2, 3, 1, 9, 7, 6]))


""" 
1)
2546; 
len=4, mid=2, left=(2,5 -> len=2, mid=1, left=2, right=5 -> merge(2,5) -> result=[2,5])
len=4, mid=2, right=(4,6 -> len=2, mid=1, left=4, right=6 -> merge(4,6) -> result=[4,6])

merge([2,5], [4,6])
i=0, j=0
2<4 -> result = [2], i=1 & j=0 -> 5 > 4 -> result = [2,4], i=1 & j=1, -> 5 < 6 -> result = [2, 4, 5] -> i=2, j=1

result.extend(left[2:] = None)
result.extend(right[2:] = 6) -> result = [2, 4, 5, 6]
"""
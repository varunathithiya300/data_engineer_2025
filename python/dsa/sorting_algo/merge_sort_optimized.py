def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    if left[-1] < right[0]:
        return left + right
    else:
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

print(merge_sort([1, -199, 2, 4, 5, 0, 9]))
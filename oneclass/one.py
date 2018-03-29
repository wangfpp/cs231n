#coding UTF-8#
def sort (arr) :
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) / 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort(left) + middle + sort(right)
print sort([12,56,8,24,1,71,25])
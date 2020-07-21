def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] is target:
            return i
    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    front = 0
    back = len(arr) - 1
    middle = None

    while front <= back:
        middle = front + back // 2

        if arr[middle] > target:
            back = middle - 1

        elif arr[middle] < target:
            front = middle + 1

        else:
            return middle

    return -1  # not found

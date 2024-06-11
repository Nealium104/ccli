def binary_search(arr, target):
    high = len(arr) - 1
    low = 0

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return mid
    return None

print(binary_search([0,1,5,16,23,32,43], 5))

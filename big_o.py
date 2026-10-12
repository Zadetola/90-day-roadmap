def binary_search(items, target):
    low = 0
    high = len(items) - 1
    while low <= high:
        middle = (low + high) // 2
        if items[middle] == target:
         return middle
        elif items[middle] < target:
          low = middle+1
        else:
          high = middle-1
    return -1

print(binary_search([4, 8, 15, 16, 23, 42], 23))
print(binary_search([4, 8, 15, 16, 23, 42], 99))
print(binary_search([4, 8, 15, 16, 23, 42], 8))
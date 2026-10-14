def bubble_sort(items):
    for p in range(len(items) - 1):
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items

print(bubble_sort([4, 3, 1]))
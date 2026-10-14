def bubble_sort(items):
    for p in range(len(items) - 1):
        for i in range(len(items) - 1):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]
    return items

print(bubble_sort([4, 3, 1]))

def insertion_sort(items): 
    for i in range(1, len(items)):
        card = items[i]
        j = i - 1
        while j >= 0 and items[j] > card:
          items[j + 1] = items[j]
          j = j - 1
        items[j + 1] = card
    return items

print(insertion_sort([5,2,4]))
def find_largest(items):
        biggest = items[0]
        for number in items:
            if number > biggest:
             biggest = number
        return biggest
print(find_largest([7, 3, 9, 2]))
print(find_largest([-5, -2, -9]))

def count_vowels(text):
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in text.lower():
        if letter in vowels:
            count += 1
    return count
print(count_vowels('banana'))
print(count_vowels('APPLE'))
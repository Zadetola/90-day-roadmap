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

def is_palindrome(word):
    word=word.lower()
    return word == (word[::-1])
print(is_palindrome('level'))
print(is_palindrome('hello'))
print(is_palindrome('Madam'))

for n in range(1, 16):
        if n % 5 == 0 and n % 3 == 0:
            print('FizzBuzz')
        elif n % 3 ==0:
         print ('Fizz')
        elif n % 5 == 0:
         print ('Buzz')
        else:
         print (n)
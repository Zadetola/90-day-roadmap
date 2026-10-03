def add(a, b):
    return a + b

print(add(3, 5))

name = input('Enter your name: ')
if name == ('Nabi'):
    print('Welcome back!')
else:
    print('Who are you?')


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

print(is_even(4))

def set_name():
    name = 'Nabi'
    return name

name = set_name()
print(name)
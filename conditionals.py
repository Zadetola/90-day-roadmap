password = input('Enter a password: ')
length = len(password)
if length >= 8:
        print('Strong')
else:
    print('Weak')
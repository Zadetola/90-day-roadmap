import random
secret = random.randint(1, 100)
number = int(input('Enter your guess :'))
while number != secret:
    print('Try Again')
    number = int(input('enter new guess :'))
print('Correct!')
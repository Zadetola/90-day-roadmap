import random
play_again = 'yes'
while play_again == 'yes':
    difficulty= input('Choose your difficulty level :')
    attempts = 0
    if difficulty == 'easy':
        secret = random.randint(1, 25)
    elif difficulty == 'medium':
        secret = random.randint(1, 50)
    else:
        secret = random.randint(1, 100)
    number = int(input('Enter your guess :'))
    attempts += 1
    while number != secret:
        print('Try Again')
        number = int(input('enter new guess :'))
        attempts += 1
    print('Correct!')
    print('You got it after', attempts, 'attempts')
    play_again = input('Play again? (yes/no): ')
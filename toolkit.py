import password_generator
import strength_checker
import hash_generator
import token_generator

menu = input('choose a tool:')
if menu == '1':
       length = int(input('How many characters? '))
       print(password_generator.generate_password(length)) 

elif menu == '2':
           password = input('Enter a password to check: ')
           print(strength_checker.check_strength(password))


elif menu == '3':
           text = input('Enter a text to check: ')
           print(hash_generator.generate_hash(text))


elif menu == '4':
            length = int(input('How many characters? '))
            print(token_generator.generate_token(length))

else:
    print('Invalid choice')
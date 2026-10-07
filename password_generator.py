import random
import string
def generate_password(length):
    password = ''
    for i in range(length):
        password = password + random.choice(string.ascii_letters)
    return password
print(generate_password(8))
import random
import string
def generate_token(length):
     token= ''
     for i in range(length):
           token= token+ random.choice(string.ascii_letters + string.digits)
     return(token)
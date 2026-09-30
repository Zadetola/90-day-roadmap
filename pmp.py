import json
with open('password.json', 'r') as file:
    loaded_passwords = json.load(file)
print( loaded_passwords)
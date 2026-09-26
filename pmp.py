passwords = {'gmail': {'username': 'nabi@email.com', 'password': 'mypass123'},  'tiktok': {'username': 'zee@email.com', 'password': 'mypass13'}}
print(passwords['tiktok']['password'])
passwords['instagram'] = {'username': 'nabi_ig', 'password': 'insta456'}
print(passwords)
for service in passwords:
    print(service, passwords[service]['username'])
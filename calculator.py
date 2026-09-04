first_num = input('Enter the first number :')
second_num = input('Enter the second number :')
operation = input('Enter any operator :')

if operation == '+':
    result = int(first_num) + int(second_num)
elif operation == '-':
    result = int(first_num) - int(second_num)
elif operation == '*':
    result = int(first_num) * int(second_num)
elif operation == '/':
    result = int(first_num) / int(second_num)

print(result)
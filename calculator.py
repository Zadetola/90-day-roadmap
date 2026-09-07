def calculate(first_num, second_num, operation):
    if operation == '+':
        result = int(first_num) + int(second_num)
    elif operation == '-':
        result = int(first_num) - int(second_num)
    elif operation == '*':
        result = int(first_num) * int(second_num)
    elif operation == '/':
        result = int(first_num) / int(second_num)
    return result 
first_num = input('Enter the first number :')
second_num = input('Enter the second number :')
operation = input('Enter any operator :')
result = calculate(first_num, second_num, operation)
print(result)

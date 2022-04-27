number_1 = int(input('Enter number: '))
operator = input('Enter operator: ')
number_2 = int(input('Enter number: '))

result = None

if operator == '+':
    result = number_1 + number_2

elif operator == '-':
    result = number_1 - number_2

elif operator == '*':
    result = number_1 * number_2

elif operator == '/':
    result = number_1 / number_2

else:
    print('Invalid operator. Quitting program')
    exit()

print(f'{number_1}{operator}{number_2}={result}')

number_1 = int(input('Enter number: '))
operator = input('Enter operator: ')
number_2 = int(input('Enter number: '))

result = None

while result is None:

    if operator == '+':
        result = number_1 + number_2

    elif operator == '-':
        result = number_1 - number_2

    elif operator == '*':
        result = number_1 * number_2

    elif operator == '/':
        result = number_1 / number_2

    else:
        print('Invalid operator. Try again!')
        operator = input('Enter operator: ')

if result is not None:
    print(f'{number_1}{operator}{number_2}={result}')
else:
    print('Cannot compute')

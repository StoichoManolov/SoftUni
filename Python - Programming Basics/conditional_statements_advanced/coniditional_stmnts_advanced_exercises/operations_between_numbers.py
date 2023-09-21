number_one = int(input())
number_two = int(input())
operation = input()
result = 0

if number_two == 0 and (operation == '/' or operation == '%'):
    print(f'Cannot divide {number_one} by zero')
elif operation == '+':
    result = number_one + number_two
elif operation == '-':
    result = number_one - number_two
elif operation == '*':
    result = number_one * number_two
elif operation == '/':
    result = number_one / number_two
elif operation == '%':
    result = number_one % number_two
if operation == '+' or operation == '-' or operation == '*':
    even_or_not = result % 2
    if even_or_not == 0:
        print(f'{number_one} {operation} {number_two} = {result} - even')
    else:
        print(f'{number_one} {operation} {number_two} = {result} - odd')
elif operation == '/' and number_two != 0:
    print(f'{number_one} {operation} {number_two} = {result:.2f}')
elif operation == '%' and number_two !=0:
    print(f'{number_one} {operation} {number_two} = {result}')

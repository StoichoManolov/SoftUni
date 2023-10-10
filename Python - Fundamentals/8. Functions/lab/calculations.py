operator_input = input()
first_num = int(input())
second_num = int(input())

def solve(a, b, operator):
    result = None
    if operator_input == 'multiply':
        result = a * b
    elif operator_input == 'divide':
        result = int(a / b)
    elif operator_input == 'add':
        result = a + b
    else:
        result = a - b
    return result

print(solve(first_num, second_num, operator_input))


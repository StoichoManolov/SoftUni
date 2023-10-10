import math

def factorial_num(a=int(input()), b=int(input())):
    a_total = math.factorial(a)
    b_total = math.factorial(b)
    result = a_total / b_total
    return result

print(f'{factorial_num():.2f}')




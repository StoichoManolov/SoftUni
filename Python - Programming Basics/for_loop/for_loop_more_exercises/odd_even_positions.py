from sys import maxsize
n = int(input())
odd_sum = 0
odd_min = maxsize
odd_max = - maxsize
even_sum = 0
even_max = - maxsize
even_min = maxsize

for numbers in range(1, n + 1):
    number = float(input())
    if numbers % 2.00 == 0.00:
        even_sum += number
        if even_min > number:
            even_min = number
        if even_max < number:
            even_max = number
    else:
        odd_sum += number
        if odd_min > number:
            odd_min = number
        if odd_max < number:
            odd_max = number

print(f'OddSum={odd_sum:.2f},')
if odd_min == maxsize and odd_max == - maxsize:
    print(f'OddMin=No,')
    print(f'OddMax=No,')
else:
    print(f'OddMin={odd_min:.2f},')
    print(f'OddMax={odd_max:.2f},')
print(f'EvenSum={even_sum:.2f},')
if even_max == - maxsize and even_min == maxsize:
    print(f'EvenMin=No,')
    print(f'EvenMax=No')
else:
    print(f'EvenMin={even_min:.2f},')
    print(f'EvenMax={even_max:.2f}')


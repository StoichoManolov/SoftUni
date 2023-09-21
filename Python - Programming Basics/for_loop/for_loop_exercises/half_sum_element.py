import sys
from sys import maxsize

number_count = int(input())
max_number = - sys.maxsize
total_sum = 0

for number in range(0, number_count):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number

if max_number == total_sum - max_number:
    print(f'Yes')
    print(f'Sum = {total_sum - max_number}')
else:
    print(f'No')
    diff = total_sum - max_number
    print(f'Diff = {abs(diff - max_number)}')



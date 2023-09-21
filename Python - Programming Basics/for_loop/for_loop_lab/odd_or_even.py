numbers = int(input())
odd_sum = 0
even_sum = 0

for number in range(numbers):
    current_number = int(input())
    if number % 2 == 0:
        even_sum += current_number
    else:
        odd_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f'Sum = {odd_sum}')
elif odd_sum > even_sum or even_sum > odd_sum:
    print('No')
    diff = odd_sum - even_sum
    print(f'Diff = {abs(diff)}')



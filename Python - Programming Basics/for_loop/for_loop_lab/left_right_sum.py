numbers = int(input())
total_sum1 = 0
total_sum2 = 0

for number in range(numbers*2):
    current_number1 = int(input())
    if number < numbers:
        total_sum1 += current_number1
    else:
        total_sum2 += current_number1


if total_sum1 == total_sum2:
    print(f'Yes, sum = {total_sum1} ')
elif total_sum1 > total_sum2 or total_sum2 > total_sum1:
    diff = total_sum1 - total_sum2
    print(f'No, diff = {abs(diff)} ')
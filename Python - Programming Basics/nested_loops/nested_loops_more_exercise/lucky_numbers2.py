n = int(input())
previous_sum = 0
current_sum = 0
number = 0

for num in range(1111,10000):
    current_sum = 0
    previous_sum = 0
    num_as_str = str(num)
    for number,digit in enumerate(num_as_str):
        current_digit = int(digit)
        if current_digit == 0:
            break

        if number == 0 or number == 1:
            current_sum += current_digit
        else:
            previous_sum += current_digit

        if number == 3:
            if current_sum == previous_sum:
                if n % previous_sum != 0:
                    continue
                else:
                    print(f'{num}', end=' ')

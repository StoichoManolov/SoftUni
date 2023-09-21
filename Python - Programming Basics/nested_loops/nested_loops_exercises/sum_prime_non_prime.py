number = input()
sum_prime = 0
sum_non_prime = 0

while number != "stop":

    num = int(number)

    if num < 0:
        print(f'Number is negative.')
        number = input()
        continue

    is_prime = True
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

    if is_prime:
        sum_prime += num
    else:
        sum_non_prime += num

    number = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')


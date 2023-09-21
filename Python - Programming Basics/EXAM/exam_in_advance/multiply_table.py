n = int(input())

n_as_str = str(n)
last_number = n % 10
first_number = n // 100
middle_number = (n % 100) // 10

for number1 in range(1,last_number + 1):
    for number2 in range(1, middle_number + 1):
        for number3 in range(1, first_number + 1):
            if number3 <= 0 or number2 <= 0 or number1 <= 0:
                continue

            product = number3 * number2 * number1
            print(f'{number1} * {number2} * {number3} = {product};')




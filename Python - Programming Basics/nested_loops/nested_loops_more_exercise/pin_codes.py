n1_max = int(input())
n2_max = int(input())
n3_max = int(input())

for num in range(1, n1_max + 1):
    if num % 2 != 0:
        continue
    for num2 in range(1, n2_max + 1):
        is_prime = True
        if 1 >= num2 or num2 > 7:
            continue
        elif num2 <= 7:
            for i in range(2, num2):
                if (num2 % i) == 0:
                    is_prime = False
        if not is_prime:
            continue
        for num3 in range(1, n3_max + 1):
            if num3 % 2 == 0:
                print(f'{num} {num2} {num3}')

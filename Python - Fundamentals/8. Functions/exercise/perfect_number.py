number = int(input())

def is_perfect(num):
    is_it_perfect = False
    total = 0
    for n in range(1, num - 1):
        if num % n == 0:
            total += n

    if total == num:
        is_it_perfect = True

    return is_it_perfect

if is_perfect(number):
    print(f'We have a perfect number!')
else:
    print(f"It's not so perfect.")


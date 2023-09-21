start_number = int(input())
end_number = int(input())

for num1 in range(start_number, end_number + 1):
    for num2 in range(start_number, end_number + 1):
        total = 0
        for num3 in range(start_number, end_number + 1):
            total = num3 + num2
            for num4 in range(start_number, end_number + 1):

                if num1 % 2 == 0 and num4 % 2 == 0:
                    continue
                elif num1 % 2 != 0 and num4 % 2 != 0:
                    continue
                if num4 > num1:
                    continue
                if total % 2 == 0:
                    print(f'{num1}{num2}{num3}{num4}', end=" ")






first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):
    ascii_value = chr(num)
    print(f"{ascii_value}", end=" ")

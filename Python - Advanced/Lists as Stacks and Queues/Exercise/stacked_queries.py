lines = int(input())
numbers = []

for i in range(lines):
    number = input().split()
    command = number[0]

    if command == "1":
        numbers.append(number[1])
    elif command == "2":
        if numbers:
            numbers.pop()
        else:
            continue
    elif command == "3":
        if numbers:
            max_numb = max(numbers)
            print(max_numb)
    elif command == "4":
        if numbers:
            min_num = min(numbers)
            print(min_num)

numbers.reverse()

print(*numbers, sep=", ")

# numbers = []
#
# for _ in range(int(input())):
#     numbers_data = input().split()  # "1 97" -> ["1", "97"] -> [1, 97]
#     command = numbers_data[0]
#
#     if command == "1":
#         numbers.append(numbers_data[1])
#     elif command == "2":
#         if numbers:
#             numbers.pop()
#     elif command == "3":
#         if numbers:
#             print(max(numbers))
#     elif command == "4":
#         if numbers:
#             print(min(numbers))
#
# numbers.reverse()
#
# print(*numbers, sep=", ")


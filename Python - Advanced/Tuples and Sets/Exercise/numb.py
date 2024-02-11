first_set = set(int(x) for x in input().split())
second_set = set(int(x) for x in input().split())

number = int(input())

for _ in range(number):

    first_command, second_command, *data = input().split()

    if first_command == 'Add':
        if second_command == 'First':
            [first_set.add(int(el)) for el in data]
        elif second_command == 'Second':
            [second_set.add(int(el)) for el in data]

    elif first_command == 'Remove':
        if second_command == 'First':
            [first_set.discard(int(el)) for el in data]
        elif second_command == 'Second':
            [second_set.discard(int(el)) for el in data]

    elif first_command == 'Check':
        print(first_set.issubset(second_set) or second_set.issubset(first_set))

print(*sorted(first_set), sep=", ")
print(*sorted(second_set), sep=", ")


# set_one = set(int(x) for x in input().split())
# set_two = set(int(x) for x in input().split())
#
# number = int(input())
#
# for _ in range(number):
#
#     first_command, second_command, *data = input().split()
#
#     if first_command == 'Add':
#         if second_command == 'First':
#             for i in data:
#                 set_one.add(int(i))
#         elif second_command == 'Second':
#             for i in data:
#                 set_two.add(int(i))
#
#     elif first_command == 'Remove':
#         if second_command == 'First':
#             for i in data:
#                 set_one.discard(int(i))
#         elif second_command == 'Second':
#             for i in data:
#                 set_two.discard(int(i))
#
#     elif first_command == 'Check':
#         print(set_one.issubset(set_two) or set_two.issubset(set_one))
#
# print(*sorted(set_one), sep=', ')
# print(*sorted(set_two), sep=', ')
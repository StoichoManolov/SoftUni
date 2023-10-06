# integers = input().split()
# n_number = int(input())
#
# list_as_integers = []
#
# for num in integers:
#     list_as_integers.append(int(num))
#
# list_as_integers.sort(reverse=True)
#
# for number in range(n_number):
#     list_as_integers.pop()
#
# print(list_as_integers)
#
lowest_numbers = []
integers = input().split()
n_number = int(input())

list_as_integers = []

for num in integers:
    list_as_integers.append(int(num))

for _ in range(n_number):
    list_as_integers.remove(min(list_as_integers))

# for n in list_as_integers:
#     print(f'{n}', end=', ')

print(*list_as_integers, sep=', ')  # unpacks the list item by item, using sep to separate items by comma and space.



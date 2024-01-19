sets_length = [int(x) for x in input().split()]

set_one = set()
set_two = set()

for one in range(sets_length[0]):
    numbers = int(input())
    set_one.add(numbers)

for two in range(sets_length[1]):
    number = int(input())
    set_two.add(number)

same = set_one & set_two

for item in same:
    print(item)
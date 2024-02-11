number = int(input())
even_set = set()
odd_set = set()

for row in range(1, number + 1):
    ascii_ = 0
    name = input()

    for i in name:
        ascii_ += ord(i)

    ascii_ = int(ascii_ / row)

    if ascii_ % 2 == 0:
        even_set.add(ascii_)
    else:
        odd_set.add(ascii_)


if sum(even_set) > sum(odd_set):
    print(*(even_set ^ odd_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*(odd_set - even_set), sep=', ')
else:
    print(*(even_set | odd_set), sep=', ')
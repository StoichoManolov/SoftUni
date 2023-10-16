string = input().split(', ')

sorting_list = sorted(string, key=lambda  x: (-len(x), x))

print(sorting_list)
numbers = tuple([float(x) for x in input().split()])

num_values = {}

for i in numbers:
    if i not in num_values:
        num_values[i] = numbers.count(i)

for number,value in num_values.items():
    print(f'{number} - {value} times')


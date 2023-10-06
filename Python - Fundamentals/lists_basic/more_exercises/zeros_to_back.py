single_string = input().split(', ')
new_string = []

for item in single_string:
    new_item = int(item)
    if new_item != 0:
        new_string.append(new_item)


for zero in single_string:
    new_zero = int(zero)
    if new_zero == 0:
        new_string.append(new_zero)


print(new_string)



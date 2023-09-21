divider = int(input())
max_number = int(input())
largest = 0

for num in range(divider + 1, max_number + 1):
    if num == 0:
        continue
    elif num % divider == 0 and max_number >= num > 0:
        if num > largest:
            largest = num
print(largest)
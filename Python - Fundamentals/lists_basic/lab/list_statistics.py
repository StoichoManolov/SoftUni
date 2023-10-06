num = int(input())

positive_list = []
negative_list = []

for n in range(num):
    numbers = int(input())

    if 0 > numbers:
        negative_list.append(numbers)
    else:
        positive_list.append(numbers)

print(positive_list)
print(negative_list)
print(f'Count of positives: {len(positive_list)}')
print(f'Sum of negatives: {sum(negative_list)}')





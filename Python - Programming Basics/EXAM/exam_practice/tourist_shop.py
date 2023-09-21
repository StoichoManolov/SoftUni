numbers = int(input())

total_numbers = 0
divided_by_2 = 0
divided_by_3 = 0
divided_by_4 = 0

for number in range(numbers):
    current_number = int(input())
    total_numbers += 1
    if current_number % 2 == 0:
        divided_by_2 += 1
    if current_number % 3 == 0:
        divided_by_3 += 1
    if current_number % 4 == 0:
        divided_by_4 += 1

percent_by_2 = divided_by_2 / total_numbers * 100
percent_by_3 = divided_by_3 / total_numbers * 100
percent_by_4 = divided_by_4 / total_numbers * 100

print(f'{percent_by_2:.2f}%')
print(f'{percent_by_3:.2f}%')
print(f'{percent_by_4:.2f}%')

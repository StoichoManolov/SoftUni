numbers = int(input())
percent = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for n in range(numbers):
    current_number = int(input())
    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    elif current_number >= 800:
        p5 += 1

total_numbers = p1 + p2 + p3 + p4 + p5


print(f'{p1 / total_numbers * 100:.2f}%')
print(f'{p2 / total_numbers * 100:.2f}%')
print(f'{p3 / total_numbers * 100:.2f}%')
print(f'{p4 / total_numbers * 100:.2f}%')
print(f'{p5 / total_numbers * 100:.2f}%')


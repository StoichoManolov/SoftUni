num = int(input())
list_of_numbers = []
filtered_numbers = []
num = int(input())
list_of_numbers = []
filtered_numbers = []

for n in range(num):
    numbers = int(input())
    list_of_numbers.append(numbers)

command = input()

if command == 'even':
    for number in list_of_numbers:
        if number % 2 == 0:
            filtered_numbers.append(number)
elif command == 'odd':
    for number in list_of_numbers:
        if number % 2 != 0:
            filtered_numbers.append(number)
elif command == 'positive':
    for number in list_of_numbers:
        if number >= 0:
            filtered_numbers.append(number)
elif command == 'negative':
    for number in list_of_numbers:
        if number < 0:
            filtered_numbers.append(number)
print(filtered_numbers)

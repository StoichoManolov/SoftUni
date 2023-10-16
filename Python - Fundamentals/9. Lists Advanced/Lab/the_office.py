employees = input().split(' ')
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employees))
filtered_list = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))

if len(filtered_list) >= len(employees) / 2 :
    print(f'Score: {len(filtered_list)} / {len(employees)}. Employees are happy!')
else:
    print(f'Score: {len(filtered_list)} / {len(employees)}. Employees are not happy!')
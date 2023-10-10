
abs_list = []
abs_command = list(map(float, input().split()))

for num in abs_command:
    abs_number = abs(num)
    abs_list.append(abs_number)

print(abs_list)
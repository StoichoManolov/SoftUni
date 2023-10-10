numbers = [float(i) for i in input().split()]

round_list = []

for num in numbers:
    round_list.append(round(num))

print(round_list)

# main_list = [float(n) for n in input().split()]
#
#
# def round_numbers(numbers):
#     result = [round(num) for num in numbers]
#     return result
#
#
# print(round_numbers(main_list))
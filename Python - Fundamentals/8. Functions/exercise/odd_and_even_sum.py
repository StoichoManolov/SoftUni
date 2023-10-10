# number = int(input())
#
# def odd_even_sum(numbers):
#     odd_sum = 0
#     even_sum = 0
#     num_as_str = str(numbers)
#     for ind, item in enumerate(num_as_str):
#         if int(item) % 2 == 0:
#             even_sum += int(item)
#         else:
#             odd_sum += int(item)
#     return f'Odd sum = {odd_sum}, Even sum = {even_sum}'
#
# print(odd_even_sum(number))

number = input()

def odd_or_even(numbers):
    even_sum = 0
    odd_sum = 0
    for num in numbers:
        int_num = int(num)
        if int_num % 2 == 0:
            even_sum += int_num
        else:
            odd_sum += int_num

    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'

print(odd_or_even(number))

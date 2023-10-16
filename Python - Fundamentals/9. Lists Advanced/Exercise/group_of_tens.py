string = [int(i) for i in input().split(', ')]
start = 10
while True:

    if len(string) == 0:
        break

    numbers = []
    for num in string[:]:
        if num <= start:
            numbers.append(num)
            string.remove(num)
    else:
        print(f"Group of {start}'s: {numbers}")

    start += 10

# number_list = [int(n) for n in input().split(", ")]
#
# for n in range(1, 11):
#     check_list = list()
#     if len(number_list) != 0:
#         [check_list.append(i) for i in number_list if i <= (n * 10)]
#         [number_list.remove(o) for o in check_list]
#         print(f"Group of {n * 10}'s: {check_list}")






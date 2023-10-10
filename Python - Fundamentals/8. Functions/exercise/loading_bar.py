number = int(input())


def loading_bar(a):
    loading = ''
    if a == 100:
        loading = '[%%%%%%%%%%]'
    else:
        for n in range(a // 10):
            loading += '%'
    for i in range(1,11):
        if a == 100:
            break
        elif not len(loading) == 10:
            loading += '.'
    return loading


if number == 100:
    print(f'100% Complete!')
    print(loading_bar(number), sep='')
else:
    print(f'{number}% [{loading_bar(number)}]', sep='')
    print(f'Still loading...')


# number = int(input())
#
# def loading_bar(num):
#     target = 10
#     num_range = int(num/10)
#     if target == num_range:
#         return "100% Complete!\n" + "[" + target * '%' + ']'
#     else:
#         return f'{num}% ' + '[' + num_range * '%' + (target - num_range) * '.' + ']\n' + "Still loading..."
#
#
# print(loading_bar(number))
numbers = [int(i) for i in input().split()]

def even_numbers(list_of_ints):
    return list_of_ints % 2 == 0

even_numbers = list(filter(even_numbers, numbers))

print(even_numbers)
string_of_integers = input().split(", ")
beggars_count = int(input())
idn = 0
money_as_int = []

for num in string_of_integers:
    money_as_int.append(int(num))

final_money = []

while beggars_count > idn:
    current_money = 0
    for index in range(idn, len(string_of_integers), beggars_count):
        current_sum = money_as_int[index]
        current_money += current_sum
    else:
        final_money.append(current_money)

    idn += 1
print(final_money)




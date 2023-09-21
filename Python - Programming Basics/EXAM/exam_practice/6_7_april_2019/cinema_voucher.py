voucher_price = int(input())
total_price = 0
ticket_count = 0
other_count = 0

while True:
    film_name = input()
    name = film_name
    if film_name == 'End':
        break

    if len(name) >= 8:
        is_ticket = True
        total_price += ord(film_name[0])
        total_price += ord(film_name[1])
    else:
        is_ticket = False
        total_price += ord(film_name[0])

    if voucher_price >= total_price:
        if is_ticket:
            ticket_count += 1
        else:
            other_count += 1
    else:
        break

print(f'{ticket_count}')
print(f'{other_count}')






student = 0
standard = 0
kid = 0
total_tickets = 0
film_name = input()

while film_name != 'Finish':

    free_seats = int(input())
    type_of_ticket = input()
    current_tickets = 0
    while type_of_ticket != 'End':
        if type_of_ticket == 'standard':
            standard += 1
        elif type_of_ticket == 'student':
            student += 1
        elif type_of_ticket == 'kid':
            kid += 1
        total_tickets += 1
        current_tickets += 1
        if current_tickets >= free_seats:
            break
        type_of_ticket = input()
    percent_full = current_tickets / free_seats * 100
    print(f'{film_name} - {percent_full:.2f}% full.')
    film_name = input()

percent_students = (student / total_tickets) * 100
percent_standard = (standard / total_tickets) * 100
percent_kid = (kid / total_tickets) * 100

print(f'Total tickets: {total_tickets}')
print(f"{percent_students:.2f}% student tickets.")
print(f"{percent_standard:.2f}% standard tickets.")
print(f'{percent_kid:.2f}% kids tickets.')


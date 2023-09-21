standard = 0
kid = 0
student = 0
tickets = 0

while True:
    movie_name = input()
    if movie_name == 'Finish':
        break
    ticket_bought = int(input())
    current_tickets = 0
    while True:
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'standard':
            standard += 1
        elif ticket_type == 'student':
            student += 1
        elif ticket_type == 'kid':
            kid += 1
        current_tickets += 1
        tickets += 1
        if current_tickets >= ticket_bought:
            break

    full_area = (current_tickets / ticket_bought) * 100
    print(f'{movie_name} - {full_area:.2f}% full.')

avg_std = (standard / tickets) * 100
avg_stu = (student / tickets) * 100
avg_kid = (kid / tickets) * 100

print(f'Total tickets: {tickets:}')
print(f'{avg_stu:.2f}% student tickets.')
print(f'{avg_std:.2f}% standard tickets.')
print(f'{avg_kid:.2f}% kids tickets.')

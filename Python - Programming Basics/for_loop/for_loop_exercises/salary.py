open_tabs = int(input())
salary = int(input())
salary_after = salary
for sites in range(open_tabs):
    open_tab = input()
    if open_tab == 'Facebook':
        salary -= 150
    elif open_tab == 'Instagram':
        salary -= 100
    elif open_tab == 'Reddit':
        salary -= 50
    if salary <= 0:
        break

if salary <= 0:
    print('You have lost your salary.')
else:
    print(f'{salary}')


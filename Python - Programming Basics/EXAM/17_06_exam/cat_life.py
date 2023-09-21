from math import floor
type_of_cat = input()
gender = input()
years = 0

if type_of_cat == 'British Shorthair':
    if gender == 'm':
        years = 13
    elif gender == 'f':
        years = 14
elif type_of_cat == 'Siamese':
    if gender == 'm':
        years = 15
    elif gender == 'f':
        years = 16
elif type_of_cat == 'Persian':
    if gender == 'm':
        years = 14
    elif gender == 'f':
        years = 15
elif type_of_cat == 'Ragdoll':
    if gender == 'm':
        years = 16
    elif gender == 'f':
        years = 17
elif type_of_cat == 'American Shorthair':
    if gender == 'm':
        years = 12
    elif gender == 'f':
        years = 13
elif type_of_cat == 'Siberian':
    if gender == 'm':
        years = 11
    elif gender == 'f':
        years = 12

in_months = (years * 12) / 6

if years > 0:
    print(f'{floor(in_months)} cat months')
else:
    print(f'{type_of_cat} is invalid cat!')


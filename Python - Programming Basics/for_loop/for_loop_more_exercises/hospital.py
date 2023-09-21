period_of_time = int(input())
treated_patients = 0
untreated_patients = 0
total_patients = 0
doctors = 7


for days in range(1, period_of_time+1):
    if days % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    patients = int(input())
    if patients <= doctors:
        treated_patients += patients
    elif patients > doctors:
        untreated_patients += abs(doctors - patients)
        treated_patients += doctors

print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')


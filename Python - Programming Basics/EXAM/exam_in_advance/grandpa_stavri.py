days = int(input())

total_rakia = 0
rakia_degrees = 0

for _ in range(days):
    rakia_amount = float(input())
    degree_of_rakia = float(input())
    total_rakia += rakia_amount
    rakia_degrees += degree_of_rakia * rakia_amount

avg_degrees = rakia_degrees / total_rakia

print(f'Liter: {total_rakia:.2f}')
print(f'Degrees: {avg_degrees:.2f}')
if avg_degrees < 38:
    print(f'Not good, you should baking!')
elif avg_degrees < 42:
    print(f'Super!')
else:
    print(f'Dilution with distilled water!')



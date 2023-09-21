adults = 0
kids = 0

while True:
    command = input()

    if command == 'Christmas':
        break
    age = int(command)

    if age <= 16:
        kids += 1
    elif age > 16:
        adults += 1


kids_cost = kids * 5
adults_cost = adults * 15

print(f'Number of adults: {adults}')
print(f'Number of kids: {kids}')
print(f'Money for toys: {kids_cost}')
print(f'Money for sweaters: {adults_cost}')
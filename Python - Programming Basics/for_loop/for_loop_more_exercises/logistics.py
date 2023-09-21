amount_of_cargo = int(input())

bus = 0
truck = 0
train = 0

for number in range(1, amount_of_cargo + 1 ):
    cargo = int(input())
    if cargo <= 3:
        bus += cargo
    elif cargo <= 11:
        truck += cargo
    elif cargo >= 12:
        train += cargo

total_cargo = bus + train + truck
total_price = ((bus * 200) + (truck * 175) + (train * 120)) / total_cargo

print(f'{total_price:.2f}')
print(f'{bus / total_cargo * 100:.2f}%')
print(f'{truck / total_cargo * 100:.2f}%')
print(f'{train / total_cargo * 100:.2f}%')

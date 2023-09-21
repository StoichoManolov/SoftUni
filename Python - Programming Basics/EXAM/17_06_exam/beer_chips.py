from math import ceil

fan_name = input()
budget = float(input())
beer = int(input())
snacks = int(input())

beer_price = beer * 1.20
packet_snack = beer_price * 0.45
packets_price = ceil(packet_snack * snacks)

total = packets_price + beer_price

diff = abs(total - budget)

if budget >= total:
    print(f'{fan_name} bought a snack and has {diff:.2f} leva left.')
else:
    print(f'{fan_name} needs {diff:.2f} more leva!')


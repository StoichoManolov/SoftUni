from math import ceil

people_amount = int(input())
entry_tax = float(input())
price_sun_lounger = float(input())
price_umbrella = float(input())

sun_loungers = (ceil(people_amount * 0.75))
sun_loungers *= price_sun_lounger

umbrellas = (ceil(people_amount * 0.5)) * price_umbrella

total_price = umbrellas + sun_loungers + (entry_tax * people_amount)

print(f'{total_price:.2f} lv.')
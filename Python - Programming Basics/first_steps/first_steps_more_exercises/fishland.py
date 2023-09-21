skumriq_price_per_kg = float(input())
caca_price_per_kg = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

midi_price_per_kg = 7.50

palamud_price = skumriq_price_per_kg + (skumriq_price_per_kg * 0.6)
safrid_price = caca_price_per_kg + (caca_price_per_kg * 0.8)

palamud_bought = palamud_kg * palamud_price
safrid_bought = safrid_price * safrid_kg
midi_price = midi_price_per_kg * midi_kg

total = palamud_bought + safrid_bought + midi_price

print(f'{total:.2f}')


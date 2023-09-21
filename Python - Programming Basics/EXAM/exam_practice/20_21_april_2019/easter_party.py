guest = int(input())
price_per_guest = float(input())
budget = float(input())

cake_price = budget * 0.10


if 10 <= guest <= 15:
    price_per_guest *= 0.85
elif 15 < guest <= 20:
    price_per_guest *= 0.80
elif guest >= 20:
    price_per_guest *= 0.75


money_needed = (price_per_guest * guest) + cake_price
diff = abs(money_needed - budget)
if money_needed < budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f"No party! {diff:.2f} leva needed.")



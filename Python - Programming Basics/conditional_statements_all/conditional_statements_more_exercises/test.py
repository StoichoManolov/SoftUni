n = int(input())
day_or_night = input()

if n >= 100:
    train_price = 0.06 * n
    print(f"{train_price:.2f}")
elif n >= 20:
    bus_price = 0.09 * n
    print(f"{bus_price:.2f}")

else:
    taxi_price = 0.7
    if day_or_night == 'day':
        taxi_price = taxi_price + (0.79 * n)
    elif day_or_night == 'night':
        taxi_price = taxi_price + (0.9 * n)
    print(f"{taxi_price:.2f}")

print(type(taxi_price))
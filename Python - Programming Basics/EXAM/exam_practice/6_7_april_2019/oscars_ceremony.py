rent = int(input())

oscars = rent * 0.70
food = oscars * 0.85
sound = food * 0.5

total = rent + oscars + food + sound

print(f'{total:.2f}')
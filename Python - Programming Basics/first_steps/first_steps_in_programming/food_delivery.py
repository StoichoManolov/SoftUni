chicken = int(input())
fish = int(input())
vegetarian = int(input())
chicken_price = chicken * 10.35
fish_price = fish * 12.40
vegetarian_price = vegetarian * 8.15
delivery = 2.50
menus_price = fish_price + chicken_price + vegetarian_price
desert = menus_price * 0.20
total = menus_price + desert + delivery
print(total)
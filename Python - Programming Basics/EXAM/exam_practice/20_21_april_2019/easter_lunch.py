bread = int(input())
eggs = int(input())
biscuits = int(input())

bread_price = bread * 3.20
eggs_price = eggs * 4.35
biscuits_price = biscuits * 5.40

eggs_paint = (eggs * 12) * 0.15

total = bread_price + eggs_price + biscuits_price + eggs_paint
print(f'{total:.2f}')


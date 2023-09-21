flour_price = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
yeast = int(input())

sugar_price_kg = flour_price * 0.75
eggs_price = flour_price * 1.1
yeast_price = sugar_price_kg * 0.20

total_sugar = sugar_price_kg * kg_sugar
total_eggs = eggs * eggs_price
total_yeast = yeast * yeast_price
total_flour = flour_price * kg_flour

total_all = total_sugar + total_eggs + total_yeast + total_flour

print(f'{total_all:.2f}')
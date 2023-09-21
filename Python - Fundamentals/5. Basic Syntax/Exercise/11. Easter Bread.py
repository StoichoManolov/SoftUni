budget = float(input())
one_kg_flour = float(input())

price_of_pack_eggs = one_kg_flour * 0.75
one_kg_milk = (one_kg_flour * 1.25) / 4

current_loaves = 0
colored_eggs = 0

while True:

    bread = price_of_pack_eggs + one_kg_flour + one_kg_milk
    if bread > budget:
        break
    budget -= bread

    current_loaves += 1
    colored_eggs += 3
    if current_loaves % 3 == 0:
        colored_eggs -= current_loaves - 2


print(f'You made {current_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')


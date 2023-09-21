needed_plastic = int(input())
needed_paint = int(input())
needed_thinner = int(input())
work_hours = int(input())

plastic = (needed_plastic + 2) * 1.50
paint = (needed_paint + needed_paint / 10) * 14.50
thinner = needed_thinner * 5.00
bags = 0.40
utility_cost = plastic + paint + thinner + bags
workers = (utility_cost * 0.30) * work_hours

total = workers + utility_cost
print(total)

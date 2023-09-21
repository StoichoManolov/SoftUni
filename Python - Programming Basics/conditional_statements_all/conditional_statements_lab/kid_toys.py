PUZZLE = 2.60
DOLL = 3
TEDDY_BEAR = 4.10
MINION = 8.20
TRUCK = 2

excursion = float(input())
puzzles_count = int(input())
dolls_count = int(input())
teddy_bears_count = int(input())
minions_count = int(input())
trucks_count = int(input())

total_sum = (puzzles_count * PUZZLE) + (dolls_count * DOLL) + (teddy_bears_count * TEDDY_BEAR) + (minions_count * MINION) + (trucks_count * TRUCK)
discount = 0
total_toys = puzzles_count + dolls_count + teddy_bears_count + minions_count + trucks_count
if total_toys >= 50:
    discount = 0.25

total_sum_with_discount = total_sum * (1 - discount)
rent = total_sum_with_discount * 0.10
final_income = total_sum_with_discount - rent
if final_income >= excursion:
    print(f'Yes! {final_income - excursion :.2f} lv left.')
else:
    print(f'Not enough money! {excursion - final_income :.2f} lv needed.')
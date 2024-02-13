from collections import deque

daily_portions_of_food = [int(x) for x in input().split(',')]
daily_stamina = deque(int(x) for x in input().split(','))

peaks = []
climbed = False

peaks_level = [
    ['Vihren',80],['Kutelo',90],['Banski Suhodol',100],
    ['Polezhan',60],['Kamenitza',70]
]

while daily_stamina and daily_portions_of_food:

    current_portion = daily_portions_of_food.pop()
    current_stamina = daily_stamina.popleft()

    result = current_stamina + current_portion

    if result >= peaks_level[0][1]:
        peaks.append(peaks_level[0][0])
        peaks_level.pop(0)
    else:
        continue

    if len(peaks_level) == 0:
        climbed = True
        break


if climbed:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks:
    print('Conquered peaks:')
    print('\n'.join(peaks))

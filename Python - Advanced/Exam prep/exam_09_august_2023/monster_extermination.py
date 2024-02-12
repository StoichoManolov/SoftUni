from collections import deque

monster_armor = deque(int(x) for x in input().split(','))
soldier_strike = [int(x) for x in input().split(',')]
monsters_killed = 0

while monster_armor and soldier_strike:

    current_monster = monster_armor.popleft()
    current_strike = soldier_strike.pop()

    if current_strike >= current_monster:
        monsters_killed += 1
        diff = current_strike - current_monster
        if soldier_strike:
            soldier_strike[-1] += diff
        elif not soldier_strike and diff > 0:
            soldier_strike.append(diff)
    elif current_strike < current_monster:
        diff = current_monster - current_strike
        monster_armor.append(diff)

if not monster_armor:
    print(f"All monsters have been killed!")
if not soldier_strike:
    print(f"The soldier has been defeated.")

print(f'Total monsters killed: {monsters_killed}')




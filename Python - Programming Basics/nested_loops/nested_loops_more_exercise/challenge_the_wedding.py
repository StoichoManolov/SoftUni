number_of_men = int(input())
number_of_women = int(input())
max_tables = int(input())
combinations = 0

while max_tables > combinations:
    for m in range (1,number_of_men + 1):
        for w in range(1,number_of_women + 1):
            combinations += 1
            if combinations > max_tables:
                break
            print(f'({m} <-> {w})', end=" ")
    if combinations >= max_tables:
        break





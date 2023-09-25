year = int(input())

while True:

    year += 1
    year_str = str(year)
# set removes same numbers eg: 9122(len 4) -> 912 (len 3)
    if len(set(year_str)) == len(year_str):
        break
print(year)




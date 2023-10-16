electrons = int(input())
electron_distribution = []
index = 1

while True:
    if electrons <= 0:
        break

    result = 2 * index ** 2
    if result > electrons:
        result = electrons

    electron_distribution.append(result)
    electrons -= result

    index += 1

print(electron_distribution)

number = int(input())

elements = set()

for elem in range(number):
    element = input().split()

    for item in element:
        elements.add(item)

for elem in elements:
    print(elem)

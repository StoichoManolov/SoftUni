number = int(input())

names = set()


for _ in range(number):
    name = input()

    names.add(name)

for i in names:
    print(i)
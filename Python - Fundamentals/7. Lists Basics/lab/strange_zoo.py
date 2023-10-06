zoo = []

for _ in range(3):
    data = input()

    zoo.append(data)

zoo[0], zoo[2] = zoo[2], zoo[0]

print(zoo)
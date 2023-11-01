people_for_lift = int(input())
empty_spots = [int(x) for x in input().split()]
index = 0
empty_spot = 0

for x in empty_spots:

    for i in range(1, 5):
        if not people_for_lift > 0:
            break
        if empty_spots[index] == 4:
            break
        else:
            empty_spots[index] += 1
            people_for_lift -= 1
    index += 1

for x in empty_spots:
    if x < 4:
        empty_spot += 1


if int(empty_spot) > 0:
    print(f'The lift has empty spots!')
elif people_for_lift > 0:
    print(f"There isn't enough space! {people_for_lift} people in a queue!")


print(*empty_spots)
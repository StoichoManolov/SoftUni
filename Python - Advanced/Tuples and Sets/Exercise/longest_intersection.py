number = int(input())
longest = []

for _ in range(number):
    set_one = set()
    set_two = set()

    intersections = input().split('-')
    first_start, first_end = intersections[0].split(',')
    second_start,second_end = intersections[1].split(',')

    for first in range(int(first_start), int(first_end) + 1):
        set_one.add(first)

    for second in range(int(second_start),int(second_end) + 1):
        set_two.add(second)

    intersection = set_one & set_two

    if len(intersection) > len(longest):
        longest.clear()
        for i in intersection:
            longest.append(str(i))

print(f"Longest intersection is [{', '.join(longest)}] with length {len(longest)}")
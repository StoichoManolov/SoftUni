from collections import deque

single_task_time = deque(int(x) for x in input().split())
number_of_tasks = [int(x) for x in input().split()]

vader_ducky = 0
thor = 0
big_blue_rubber = 0
small_yellow_rubber = 0

while single_task_time and number_of_tasks:

    current_task_time = single_task_time.popleft()
    current_task = number_of_tasks.pop()

    result = current_task * current_task_time

    if 0 <= result <= 60:
        vader_ducky += 1
    elif 61 <= result <= 120:
        thor += 1
    elif 121 <= result <= 180:
        big_blue_rubber += 1
    elif 181 <= result <= 240:
        small_yellow_rubber += 1
    else:
        single_task_time.append(current_task_time)
        current_task -= 2
        number_of_tasks.append(current_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f'Darth Vader Ducky: {vader_ducky}')
print(f'Thor Ducky: {thor}')
print(f'Big Blue Rubber Ducky: {big_blue_rubber}')
print(f'Small Yellow Rubber Ducky: {small_yellow_rubber}')
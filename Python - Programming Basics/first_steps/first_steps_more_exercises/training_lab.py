w = float(input())
h = float(input())
work_space = 70

h_in_cm = h * 100
h_with_hallway = h_in_cm - 100
h_work_space = h_with_hallway // work_space

w_in_cm = w * 100
work_space_w = 120

work_space_w_all = w_in_cm // work_space_w

space_left = h_work_space * work_space_w_all - 3

print(f'{int(space_left)}')



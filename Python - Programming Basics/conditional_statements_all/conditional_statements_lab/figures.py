from math import pi
figure = input()
if figure == 'square':
    side = float(input())
    area = side * side
    print(f'{area:.3f}')
elif figure == 'rectangle':
    first_side = float(input())
    second_side = float(input())
    area = first_side * second_side
    print(f'{area:.3f}')
elif figure == 'circle':
    radius = float(input())
    area = radius**2 * pi
    print(f'{area:.3f}')
elif figure == 'triangle':
    length = float(input())
    height = float(input())
    area = length * height / 2
    print(f'{area:.3f}')
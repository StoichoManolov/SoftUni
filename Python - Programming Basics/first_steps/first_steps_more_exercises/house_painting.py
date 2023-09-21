height_of_house = float(input())
length_of_side = float(input())
height_of_triangle_roof = float(input())

side_of_house = height_of_house * length_of_side
window = 1.5 * 1.5
both_sides = (2 * side_of_house) - (2 * window)

back_side = height_of_house * height_of_house
entrance = 1.2 * 2

total_back_front = (2 * back_side) - entrance
total = both_sides + total_back_front
paint_needed_sides = total / 3.4

both_roof_rectangles = 2 * (height_of_house * length_of_side)
both_triangles = 2 * (height_of_house * height_of_triangle_roof / 2)

total_rooftop = both_triangles + both_roof_rectangles
paint_rooftop = total_rooftop / 4.3

print(f'{paint_needed_sides:.2f}')
print(f'{paint_rooftop:.2f}')

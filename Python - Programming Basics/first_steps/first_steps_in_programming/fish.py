length = int(input())
width = int(input())
height = int(input())
percent_taken = float(input())

volume = length * width * height
volume_water = volume * 0.001
liters_needed = volume_water * (1 - (percent_taken/100))

print(liters_needed)

import re

text = input()

pattern = r'(=|/)(?P<city>[A-Z][A-Za-z]{2,})\1'
results = []
regex = re.finditer(pattern,text)

travel_points = 0

for i in regex:
    travel_points += len(i['city'])
    results.append(i['city'])

print(f"Destinations: {', '.join(results)}")
print(f'Travel Points: {travel_points}')


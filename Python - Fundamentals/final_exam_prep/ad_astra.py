import re

calories = 0
string = input()
lists = []
pattern = r'(#|\|)(?P<name>[A-Za-z\s?]+)(\1)(?P<date>(\d{2})\/\d{2}\/\d{2})(\1)(?P<calories>\d+)(\1)'

regex = re.finditer(pattern, string)

for show in regex:
    calories += int(show["calories"])
    lists.append({"name": show["name"], "date": show["date"], "nutrition": show["calories"]})


total = int(calories // 2000)

print(f"You have food to last you for: {total} days!")
for show in lists:
    print(f"Item: {show['name']}, Best before: {show['date']}, Nutrition: {show['nutrition']}")

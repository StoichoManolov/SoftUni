import re

text = input()

pattern = r'(?P<day>\d{2})(?P<separator>[-\s/.])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})'

regex = re.finditer(pattern, text)

for match in regex:
    current_date = match.groupdict()
    print(f"Day: {current_date['day']}, Month: {current_date['month']}, Year: {current_date['year']}")

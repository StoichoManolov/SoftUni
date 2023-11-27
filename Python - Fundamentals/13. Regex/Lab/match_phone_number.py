import re

text = input()

pattern = r'(\+359 2 \d{3} \d{4}\b)|(\+359-2-\d{3}-\d{4}\b)'

search = re.finditer(pattern,text)

matches = [x.group() for x in search]

print(', '.join(matches))
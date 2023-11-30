import re
text = input()
pattern = r'(\:{2}|\*{2})([A-Z][a-z]{2,})(\1)'
pattern_two = r'\d'
cool_threshold = 1
cool_ones = []
regex = re.findall(pattern, text)
numbers = re.findall(pattern_two,text)

numbers_for_threshold = [int(x) for x in numbers]
for number in numbers_for_threshold:
    cool_threshold = cool_threshold * number

for item in regex:
    ascii_value = 0
    for letter in item[1]:
        ascii_value += ord(letter)
    if ascii_value >= cool_threshold:
        cool_ones.append(item)

print(f'Cool threshold: {cool_threshold}')
print(f'{len(regex)} emojis found in the text. The cool ones are:')
for item in cool_ones:
    print(''.join(item))
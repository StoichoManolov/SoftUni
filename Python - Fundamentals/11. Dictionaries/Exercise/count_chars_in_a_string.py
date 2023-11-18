text = input().split()

chars = {}

for i in text:
    for letter in i:
        if letter not in chars:
            chars[letter] = 0
        chars[letter] += 1

for item, value in chars.items():
    print(f'{item} -> {value}')
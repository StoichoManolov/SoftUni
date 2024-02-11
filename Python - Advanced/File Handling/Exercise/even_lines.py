import os

symbols = ("-", ",", ".", "!", "?")

with open("files/text_even_lines.txt") as file:
    strings = file.readlines()

for row in range(0, len(strings), 2):

    for symbol in symbols:
        strings[row] = strings[row].replace(symbol, "@")

    print(*strings[row].split()[::-1])
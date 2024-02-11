from string import punctuation
import os

text = os.path.join('files','text_even_lines.txt' )
output_file = os.path.join('files','output.txt')

with open(text) as file:
    strings = file.readlines()

for i in range(len(strings)):
    letters = 0
    marks = 0

    for symbol in strings[i]:
        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    with open(output_file, 'a') as text:
        text.write(f"Line{i + 1}: {''.join(strings[i][:-1])} ({letters})({marks})\n")
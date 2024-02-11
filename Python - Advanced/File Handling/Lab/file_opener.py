import os
import re

words_path = os.path.join('..','Exercise','words.txt')
text = os.path.join('..','Exercise','text_even_lines.txt')
output = os.path.join('..','Exercise','output.txt')

with open(words_path) as file:
    searched_words_as_text = file.read()
    searched_words = [word.lower() for word in searched_words_as_text.split()]


with open(text) as file:
    content = file.read().lower()


words_count = {}

for searched_word in searched_words:
    pattern = re.compile(rf'\b{searched_word}\b')
    results = re.findall(pattern,content)
    words_count[searched_word] = results.count(searched_word)

sorted_words_count = sorted(words_count.items(), key=lambda kvp: -kvp[1])

with open(output, 'a') as file:
    for word,count in sorted_words_count:
        file.write(f'{word} - {count}\n')

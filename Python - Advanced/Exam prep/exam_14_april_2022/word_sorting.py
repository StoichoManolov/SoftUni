def words_sorting(*args):

    words = {}
    output = []

    for word in args:

        if word not in words:
            words[word] = 0
        total = 0
        for letter in word:
            total += ord(letter)

        words[word] = total

    sorting = sorted(words.items(), key=lambda x: (-x[1] if sum(words.values()) % 2 != 0 else x[0]))

    for word,amount in sorting:
        output.append(f'{word} - {amount}')

    return '\n'.join(output)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

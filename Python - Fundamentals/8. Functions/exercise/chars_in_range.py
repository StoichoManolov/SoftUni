first_char = input()
second_char = input()

ascii_chars = []

def ascii_range(start, finish):

    start_ascii = ord(start) + 1
    finish_ascii = ord(finish)

    for num in range(start_ascii, finish_ascii):
        ascii_as_char = chr(num)
        ascii_chars.append(ascii_as_char)
    return ascii_chars


print(*ascii_range(first_char, second_char))

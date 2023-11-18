# ascii_chars = input().split(', ')
#
# ascii_dict = {i: ord(i) for i in ascii_chars}
#
# print(ascii_dict)

ascii_chars = input().split(', ')
ascii_dict = {}

for i in ascii_chars:
    key = i
    value = ord(i)
    ascii_dict[i] = value

print(ascii_dict)
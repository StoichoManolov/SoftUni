string = input()

encrypted = ''

for char in string:

    ascii_table = ord(char) + 3
    encrypted += chr(ascii_table)

print(encrypted)


# string = input()
#
# encrypted_text = ''
#
# for index in range(len(string)):
#     encrypted_text += chr(ord(string[index]) + 3)
#
#
# print(encrypted_text)
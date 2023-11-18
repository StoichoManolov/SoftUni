def first_letter(first, num):
    if first.isupper():
        num /= ord(first) - 64
    else:
        num *= ord(first) - 96
    return num


def last_letter(last,num):
    if last.isupper():
        num -= ord(last) - 64
    else:
        num += ord(last) - 96
    return num


string = input().split()

total = 0

for word in string:
    number = int(word[1:-1])
    number = first_letter(word[0], number)
    number = last_letter(word[-1], number)
    total += number

print(f"{total:.2f}")

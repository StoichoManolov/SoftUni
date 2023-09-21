a = input()
b = input()
c = input()
combinations = 0

a_to_ord = ord(a)
b_to_ord = ord(b)
c_to_ord = ord(c)


for letter1 in range(a_to_ord,b_to_ord + 1):
    if letter1 == c_to_ord:
        continue
    for letter2 in range(a_to_ord,b_to_ord +1 ):
        if letter2 == c_to_ord:
            continue
        for letter3 in range(a_to_ord,b_to_ord + 1):
            if letter3 == c_to_ord:
                continue
            combinations += 1
            print(f'{chr(letter1)}{chr(letter2)}{chr(letter3)}', end=' ')
print(combinations)
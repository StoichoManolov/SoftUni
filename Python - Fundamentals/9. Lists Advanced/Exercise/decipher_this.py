password = input().split()

cracked = []

for i in password:
    list_ = []
    ascii_value = ''
    word = ''
    for symbol in i:
        if symbol.isdigit():
            ascii_value += symbol
        else:
            word += symbol
    chr_ascii = chr(int(ascii_value))
    list_ = list(word)
    list_[0],list_[-1] = list_[-1], list_[0]
    list_.insert(0, chr_ascii)
    cracked.append(''.join(list_))

print(*cracked)
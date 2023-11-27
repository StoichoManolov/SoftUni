import re

n_of_barcodes = int(input())
current_group = ''
pattern = r'@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#*'

for _ in range(n_of_barcodes):
    barcode = input()

    if re.match(pattern, barcode):
        for digit in barcode:
            if digit.isdigit():
                current_group += digit
        if current_group == '':
            print(f'Product group: 00')
        else:
            print(f'Product group: {current_group}')
        current_group = ""

    else:
        print(f'Invalid barcode')


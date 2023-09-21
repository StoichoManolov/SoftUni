a1 = int(input())
a2 = int(input())
n = int(input())

limit_symbol3 = int(n / 2) - 1

for symbol1 in range(a1, a2):
    if symbol1 % 2 == 0:
        continue
    symbol1_as_chr = chr(symbol1)
    for symbol2 in range(1, n):
        for symbol3 in range(1, limit_symbol3 + 1):

            symbol4 = ord(symbol1_as_chr)

            if symbol1 % 2 != 0 and (symbol2 + symbol3 + symbol4) % 2 != 0:
                print(f"{symbol1_as_chr}-{symbol2}{symbol3}{symbol4}")




key = int(input())

number = int(input())
decrypted = ''

for num in range(number):
    code = input()
    code_as_number = ord(code) + key
    decrypted += chr(code_as_number)

print(decrypted)
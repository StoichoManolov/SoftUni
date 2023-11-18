string = input()
string_two = input()

while string in string_two:
    string_two = string_two.replace(string, '')

print(string_two)

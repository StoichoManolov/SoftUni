input_string = input()
n = int(input())

repeat_string = lambda a, b: a * b

result = repeat_string(input_string, n)

print(result)

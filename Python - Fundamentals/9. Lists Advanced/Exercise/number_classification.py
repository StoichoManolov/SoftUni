numbers = [int(x) for x in input().split(', ')]

positive = []
negative = []
odd = []
even = []

[positive.append(num) if num >= 0 else negative.append(num) for num in numbers]
[even.append(num) if num % 2 == 0 else odd.append(num) for num in numbers]

print("Positive:", end=" ")
print(*positive, sep=", ")
print("Negative:", end=" ")
print(*negative, sep=", ")
print("Even:", end=" ")
print(*even, sep=", ")
print("Odd:", end=" ")
print(*odd, sep=", ")

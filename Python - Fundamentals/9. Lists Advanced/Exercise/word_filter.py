text = input().split()

filtered_text = [word for word in text if len(word) % 2 == 0]

for i in filtered_text:
    print(i)


# [print(text) for text in input().split() if len(text) % 2 == 0]
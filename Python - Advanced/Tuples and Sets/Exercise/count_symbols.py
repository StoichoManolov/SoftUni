text = tuple(input())

items = set()
for i in sorted(text):
    count = text.count(i)
    if i not in items:
        items.add(i)
        print(f'{i}: {count} time/s')


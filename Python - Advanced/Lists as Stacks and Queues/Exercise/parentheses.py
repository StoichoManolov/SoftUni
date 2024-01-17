from collections import deque

parentheses = deque(input())
open_per = deque()
balanced = True

while parentheses:
    item = parentheses.popleft()
    if item in '{[(':
        open_per.append(item)
    elif not open_per:
        balanced = False
        break
    else:
        if f'{open_per.pop() + item}' not in '{}()[]':
            balanced = False
            break

if balanced and not open_per:
    print('YES')
else:
    print('NO')
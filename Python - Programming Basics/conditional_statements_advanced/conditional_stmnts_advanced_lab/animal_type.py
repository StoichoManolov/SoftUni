animals = input().lower()

mammals = 'dog'
reptiles = 'crocodile', 'tortoise', 'snake'

if animals in mammals:
    print('mammal')
elif animals in reptiles:
    print('reptile')
else:
    print('unknown')
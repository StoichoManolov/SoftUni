type_of_product = input().lower()

fruit = 'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes'
vegetables = 'tomato', 'cucumber', 'pepper', 'carrot'

if type_of_product in fruit:
    print('fruit')
elif type_of_product in vegetables:
    print('vegetable')
else:
    print('unknown')
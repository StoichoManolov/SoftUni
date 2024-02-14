def shopping_cart(*args):
    result, output = {"Dessert": [], "Pizza": [], "Soup": []}, []
    for info in args:
        if info == "Stop":
            break
        meal, product = info

        if product in result[meal]:
            continue

        if any((meal == "Soup" and len(result[meal]) != 3,
                meal == "Pizza" and len(result[meal]) != 4,
                meal == "Dessert" and len(result[meal]) != 2)):
            result[meal].append(product)

    results = ''
    for s_meal, s_product in sorted(result.items(), key=lambda x: (-len(x[1]), x[0])):
        results += f"{s_meal}:\n"
        for a_product in sorted(s_product):
            results += f" - {a_product}\n"

    if any(len(x) != 0 for x in result.values()):
        return results

    return "No products in the cart!"

print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))

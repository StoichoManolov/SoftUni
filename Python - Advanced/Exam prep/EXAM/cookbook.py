def cookbook(*args):
    cuisine = {}
    output = []

    for recipe,country,products in args:
        if country not in cuisine:
            cuisine[country] = []
        cuisine[country].append([recipe,products])

    sorted_cuisine = sorted(cuisine.items(), key=lambda x: (-len(x[1]),x[0]))

    for country,values in sorted_cuisine:
        output.append(f'{country} cuisine contains {len(values)} recipes:\n')
        sorted_recipe = sorted(values)
        for recipe,products in sorted_recipe:
            output.append(f"  * {recipe} -> Ingredients: {', '.join(products)}\n")
    return ''.join(output)
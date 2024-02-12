def shop_from_grocery_list(budget,grocery_list,*args):

    bought_items = []

    for item,price in args:

        if budget >= price:
            if item in bought_items:
                continue
            elif item not in grocery_list:
                continue
            bought_items.append(item)
            budget -= price
            grocery_list.remove(item)
        else:
            break

    if not grocery_list:
        return f'Shopping is successful. Remaining budget: {budget:.2f}.'
    else:
        return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."

print(shop_from_grocery_list(
    100,
    ["tomato", "cola"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("tomato", 20.45),
))



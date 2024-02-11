def sorting_cheeses(**kwargs):
    result = ''
    sorted_result = sorted(kwargs.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cheese,quantity in sorted_result:
        result += cheese + '\n'
        for quan in sorted(quantity, reverse=True):
            result += f"{quan}\n"
    return result
print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

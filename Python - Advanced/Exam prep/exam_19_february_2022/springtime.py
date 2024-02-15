def start_spring(**kwargs):

    spring = {}

    for item,types in kwargs.items():

        if types not in spring:
            spring[types] = []

        spring[types].append(item)

    sorted_spring = sorted(spring.items(), key=lambda x: (-len(x[1]),x[0]))

    output = []

    for item,types in sorted_spring:
        output.append(f'{item}:\n')
        springs = sorted(types)
        for type in springs:
            output.append(f'-{type}\n')

    return ''.join(output)


example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))





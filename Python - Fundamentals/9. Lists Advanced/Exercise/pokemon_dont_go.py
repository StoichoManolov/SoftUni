integers = [int(x) for x in input().split()]
pokemons = []

while len(integers) != 0:

    command = int(input())

    if command >= len(integers):
        command = len(integers) - 1
        first_ind = integers[0]
        current_ind = integers[command]
        integers.pop(-1)
        integers.append(first_ind)
    elif command < 0:
        command = 0
        last_ind = integers[-1]
        current_ind = integers[command]
        integers.pop(0)
        integers.insert(0, last_ind)

    else:
        current_ind = integers[command]
        del integers[command]

    pokemons.append(current_ind)
    index = 0
    for i in integers:
        if i <= current_ind:
            integers[index] = i + current_ind
        else:
            integers[index] = i - current_ind

        index += 1
result = sum(pokemons)
print(result)


# distance_to_pokemon = [int(x) for x in input().split()]
#
# result_ = []


# while distance_to_pokemon:
#     index_ = int(input())
#     captured_pokemon = ""
#     if index_ < 0:
#         captured_pokemon = distance_to_pokemon.pop(0)
#         distance_to_pokemon.insert(0, distance_to_pokemon[-1])
#     elif index_ >= len(distance_to_pokemon):
#         captured_pokemon = distance_to_pokemon.pop(-1)
#         distance_to_pokemon.append(distance_to_pokemon[0])
#     if not captured_pokemon:
#         captured_pokemon = distance_to_pokemon.pop(index_)
#     result_.append(captured_pokemon)
#     for pos, pokemon in enumerate(distance_to_pokemon):
#         if pokemon <= captured_pokemon:
#             distance_to_pokemon[pos] += captured_pokemon
#         else:
#             distance_to_pokemon[pos] -= captured_pokemon
#
# print(sum(result_))




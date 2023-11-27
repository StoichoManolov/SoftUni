def add_piece(piece, composer, key):
    if piece in composers:
        return f'{piece} is already in the collection!'
    composers[piece] = []
    composers[piece].append(composer)
    composers[piece].append(key)
    return f'{piece} by {composer} in {key} added to the collection!'


def remove(piece):
    if piece in composers:
        del composers[piece]
        return f'Successfully removed {piece}!'
    return f"Invalid operation! {piece} does not exist in the collection."


def change_key(piece,new_key):
    if piece in composers:
        composers[piece][1] = new_key
        return f'Changed the key of {piece} to {new_key}!'
    return f'Invalid operation! {piece} does not exist in the collection.'


number_of_pieces = int(input())

composers = {}

for piece in range(number_of_pieces):
    piece_name, *info = input().split("|")
    composers[piece_name] = info


while True:
    command = input()
    if command == 'Stop':
        break

    command_split = command.split('|')

    act = command_split[0]
    pieces = command_split[1]

    if act == 'Add':
        composer = command_split[2]
        key = command_split[3]
        print(add_piece(pieces,composer,key))
    elif act == 'Remove':
        print(remove(pieces))
    elif act == 'ChangeKey':
        new_key = command_split[2]
        print(change_key(pieces, new_key))

for item in composers:
    print(f"{item} -> Composer: {composers[item][0]}, Key: {composers[item][1]}")

def accommodate_new_pets(capacity,weigh_limit,*args):
    hotel = {}
    result = ''

    for pet,kg in args:
        if weigh_limit >= kg and capacity > 0:
            if pet not in hotel:
                hotel[pet] = 0
            capacity -= 1
            hotel[pet] += 1
        elif capacity == 0:
            result += 'You did not manage to accommodate all pets!\n'
            break
    else:
        result += f'All pets are accommodated! Available capacity: {capacity}.\n'

    result += 'Accommodated pets:\n'
    for pet,count in sorted(hotel.items()):
        result += f'{pet}: {count}\n'

    return result



print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))


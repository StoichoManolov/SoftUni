def add(index, string, stop):
    if 0 <= index < len(stop):
        stop = stop[:index] + string + stop[index:]
        return stop


def remove(index, end_index, stop):

    if 0 <= index < len(stop) and 0 <= end_index < len(stop):
        stop = stop[:index] + stop[end_index + 1:]
        return stop
    return stop


def switch(old_string, new_string):

    if new_string not in stops:
        stop = stops.replace(old_string, new_string)
        return stop


stops = input()

while True:

    travel_stops = input()
    if travel_stops == 'Travel':
        print(f'Ready for world tour! Planned stops: {stops}')
        break

    command_split = travel_stops.split(':')
    command = command_split[0]

    if 'Add' in command:
        index = int(command_split[1])
        string = command_split[2]
        stops = add(index, string, stops)
        print(stops)

    elif 'Remove' in command:
        start_index = int(command_split[1])
        end_index = int(command_split[2])
        stops = remove(start_index, end_index, stops)
        print(stops)

    elif 'Switch' in command:
        old_string = command_split[1]
        new_string = command_split[2]
        stops = switch(old_string, new_string)
        print(stops)



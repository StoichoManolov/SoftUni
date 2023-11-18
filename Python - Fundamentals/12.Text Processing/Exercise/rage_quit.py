string = input()

repetitions = ''
current_string = ''
rage_message = ''

for index in range(len(string)):

    if not string[index].isdigit():
        current_string += string[index].upper()
    else:
        for next_symbol in range(index, len(string)):
            if not string[next_symbol].isdigit():
                break
            repetitions += string[next_symbol]

        rage_message += current_string * int(repetitions)
        current_string = ''
        repetitions = ''

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)



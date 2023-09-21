time = int(input())
scenes = int(input())
duration = int(input())

prep = time * 0.15

time_needed = scenes * duration + prep

diff = abs(time - time_needed)

if time_needed > time:
    print(f'Time is up! To complete the movie you need {round(diff)} minutes.')
else:
    print(f"You managed to finish the movie on time! You have {round(diff)} minutes left!")
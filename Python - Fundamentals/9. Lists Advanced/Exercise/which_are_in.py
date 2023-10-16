first_string = input().split(', ')
second_string = input().split(', ')

results = []
[results.append(n) for n in first_string for i in second_string if n in i]
results = list(dict.fromkeys(results))

print(results)

# first_string = input().split(', ')
# second_string = input().split(', ')
#
# filtered = []
#
# for word in first_string:
#     for word_two in second_string:
#         if word in word_two:
#             if word in filtered:
#                 continue
#             else:
#                 filtered.append(word)
#
# print(filtered)
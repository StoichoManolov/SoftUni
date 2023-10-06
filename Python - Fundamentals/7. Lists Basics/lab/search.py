num = int(input())

word = input()
filter_list = []

for n in range(num):
    user_input = input()

    filter_list.append(user_input)

print(filter_list)

for i in range(len(filter_list) - 1, -1 , -1):
    element = filter_list[i]
    if word not in element:
        filter_list.remove(element)
print(filter_list)




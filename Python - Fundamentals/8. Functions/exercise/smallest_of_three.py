num_one = int(input())
num_two = int(input())
num_three = int(input())

def smallest(one,two,three):
    result = min(one, two, three)
    return result

print(smallest(num_one, num_two, num_three))

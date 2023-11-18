# data = input().split()
# products = {}
# search_for = input().split()
#
# for i in range(0,len(data), 2):
#     key = data[i]
#     value = data[i + 1]
#     products[key] = int(value)
#
# for product in search_for:
#
#     if product in products:
#         print(f'We have {products[product]} of {product} left')
#     else:
#         print(f"Sorry, we don't have {product}")
#


def key_value():

    for i in range(0, len(data), 2):
        key = data[i]
        value = data[i + 1]
        products[key] = int(value)


def searching():
    for product in search_for:
        if product in products:
            print(f'We have {products[product]} of {product} left')
        else:
            print(f"Sorry, we don't have {product}")


data = input().split()
products = {}
search_for = input().split()


key_value()
searching()
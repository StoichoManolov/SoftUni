pencil = int(input())
markers = int(input())
board_cleaning = int(input())
discount = int(input())

pencil_price = pencil * 5.80
markers_price = markers * 7.20
board_cleaning_price = board_cleaning * 1.20
all_cost = pencil_price + markers_price + board_cleaning_price
discount_percentage = discount / 100
all_cost_with_discount = all_cost - (all_cost * discount_percentage)

print(all_cost_with_discount)

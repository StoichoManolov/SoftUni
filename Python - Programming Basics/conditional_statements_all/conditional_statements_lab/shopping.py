VIDEO_CARD = 250

budget = float(input())
video_cards_count = int(input())
processor_count = int(input())
ram_memory = int(input())

video_cards_price = video_cards_count * VIDEO_CARD
processor_price = video_cards_price * 0.35
ram_memory_price = video_cards_price * 0.10

processor_total_cost = processor_price * processor_count
ram_memory_cost = ram_memory_price * ram_memory
discount = 0
total_price = ram_memory_cost + processor_total_cost + video_cards_price
if processor_count < video_cards_count:
    discount = 0.15

cost = total_price * (1 - discount)

if cost <= budget:
    print(f'You have {budget - cost:.2f} leva left!')
else:
    print(f'Not enough money! You need {cost - budget:.2f} leva more!')
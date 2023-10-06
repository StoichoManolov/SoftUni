cards = input().split()
shuffles = int(input())

for shuffle in range(shuffles):
    middle_deck = len(cards) // 2
    left_pack = cards[0:middle_deck]
    right_pack = cards[middle_deck:len(cards)]
    deck_after_shuffle = []
    for card_index in range(len(left_pack)):
        deck_after_shuffle.append(left_pack[card_index])
        deck_after_shuffle.append(right_pack[card_index])
    cards = deck_after_shuffle

print(cards)



num_cards = input()

card_faces = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
card_suits = ['spades', 'clubs', 'hearts', 'diamonds']

card_index = card_faces.index(num_cards)

for face in card_faces[:card_index + 1]:
    cards_in_line = [f"{face} of {suit}" for suit in card_suits]
    print(", ".join(cards_in_line))

def compare_cards(card1, card2):
    valid_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    if card1 not in valid_cards or card2 not in valid_cards:
        raise ValueError("Invalid card value")
    
    value1 = valid_cards[card1]
    value2 = valid_cards[card2]
    
    if value1 > value2:
        return card1
    elif value2 > value1:
        return card2
    else:
        return "Equal"

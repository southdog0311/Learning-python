import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(name)s:%(lineno)d - %(message)s')
logger = logging.getLogger()

def compare_cards(card1, card2):
    valid_cards = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
    if card1 not in valid_cards or card2 not in valid_cards:
        raise ValueError("Invalid card value")
    
    value1 = valid_cards[card1]
    value2 = valid_cards[card2]
    
    if value1 > value2:
        logging.info(f"{card1} is greater than {card2}")
        return card1
    elif value2 > value1:
        logging.info(f"{card2} is greater than {card1}")
        return card2
    else:
        logging.info(f"{card1} and {card2} are equal")
        return "Equal"

if __name__ == "__main__":
    result = compare_cards('K', 'Q')
    print(result)

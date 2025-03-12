VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    # check if input is valid
    if len(hand) > 5:
        return "invalid list length"
    #for each card in hand, valid it
    score = 0
    count_of_Ace = 0
    for card in hand:
        if not card in VALID_CARDS:
            return "invalid"
        elif card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score += card
        elif card == "Ace":
            count_of_Ace += 1
        if score > 21:
            return 'bust'
    if count_of_Ace == 0:
        return score
    # process Aces
    if score + 11 + (count_of_Ace - 1) <= 21:
        return score + 11 + count_of_Ace - 1
    elif score + count_of_Ace <= 21:
        return score + count_of_Ace
    else: 
        return 'bust'

#def function to check is card is face card
def is_face_card(card):
    if card in ['Jack', 'Queen', 'King']:
        return True
    return False
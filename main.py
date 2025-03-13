VALID_CARDS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']

def blackjack_score(hand):
    # check input length
    if len(hand) > 5:
        return "invalid list length"
    score = 0
    count_of_Ace = 0

    #for each card in hand, validate card first
    for card in hand:
        if not card in VALID_CARDS:
            return "invalid"
        elif card in ['Jack', 'Queen', 'King']:
            score += 10
        elif card in [2, 3, 4, 5, 6, 7, 8, 9, 10]:
            score += card
        elif card == "Ace":
            count_of_Ace += 1
        # return if exceed 21 at any time
        if score > 21:
            return 'bust'
    if not count_of_Ace:
        return score
    # with Aces, find max and min possible scores first
    max_score = score + 11 + (count_of_Ace - 1)
    min_score = score + count_of_Ace
    if max_score <= 21:
        return max_score
    elif min_score <= 21:
        return min_score
    else:
        return "bust"
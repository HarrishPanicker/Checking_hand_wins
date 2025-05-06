def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    print(hand_1, hand_2, sep="\n")
    
    hand1_sum = 0
    hand2_sum = 0
    hand1_ace_counter = 0
    hand2_ace_counter = 0
    face_cards = ('K', 'Q', 'J')
    
    for card1 in hand_1:
        #card1 face cards
        if card1 in face_cards:
            hand1_sum += 10
        #aces
        elif card1 == 'A':
            hand1_ace_counter += 1
        else:
            hand1_sum += int(card1)
    
    for card2 in hand_2:    
        #card2 face cards      
        if card2 in face_cards:
            hand2_sum += 10
        #Aces
        elif card2 == 'A':
            hand2_ace_counter += 1
        else:
            hand2_sum += int(card2)
    
    for j in range(hand1_ace_counter):
        if hand1_sum <= (10 - j * 1):
            hand1_sum += 11
        
        else:
            hand1_sum += 1
        
    for j in range(hand2_ace_counter):
        if hand2_sum <= (10 - j * 1):
            hand2_sum += 11
        
        else:
            hand2_sum += 1

    print(hand1_sum, hand2_sum, sep="\n")
    
    print(hand1_sum > hand2_sum)

    if hand1_sum <= 21 and (hand2_sum < hand1_sum or hand2_sum > 21):
        return True
    else:
        return False

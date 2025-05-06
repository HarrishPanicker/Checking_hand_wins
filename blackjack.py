def blackjack_hand_greater_than(hand_1, hand_2):
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

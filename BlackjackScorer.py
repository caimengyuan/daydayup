'''
Scoring rules:
Number cards count as their face value (2 through 10). Jack, Queen and King count as 10. An Ace can be counted as either 1 or 11.

Return the highest score of the cards that is less than or equal to 21. If there is no score less than or euqal to 21 return the smallest score more than 21.

Examples
["A"]                           ==>  11
["A", "J"]                      ==>  21
["A", "10", "A"]                ==>  12
["5", "3", "7"]                 ==>  15
["5", "4", "3", "2", "A", "K"]  ==>  25
'''
def score_hand(cards):
    # your code here
    sum = 0
    flag = 0
    for card in cards:
        if card == 'A':
            flag += 1
        else:
            if card in ['K', 'J', 'Q']:
                sum += 10
            else:
                sum += int(card)
    while flag > 0 and flag <= 1:
        if sum < 11:
            sum += 10
            flag -= 1
        else:
            sum += 1
            flag -= 1
    print(sum)

score_hand(['A', '3'])

def score_hand(a):
    n = sum(11 if x == "A" else 10 if x in "JQK" else int(x) for x in a)
    for _ in range(a.count("A")):
        if n > 21:
            n -= 10
    return n
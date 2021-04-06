import sys
sys.stdin = open("D4_9760_input.txt", "r")

kard_suits = ['S', 'D', 'H', 'C']
kard_ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']

def straight():
    if ranks[10] == ranks[11] == ranks[12] == ranks[0] == 1:
        if ranks[9] or ranks[1]:
            return True

    if ranks[12] == ranks[0] == ranks[1] == ranks[2] == 1:
        if ranks[11] or ranks[3]:
            return True

    for i in range(9):
        if ranks[i] == ranks[i + 1] == ranks[i + 2] == ranks[i + 3] == ranks[i + 4] == 1:
            return True
    return False


T = int(input())
for test_case in range(T):
    cards = list(input().split())
    suits = [0] * 4
    ranks = [0] * 13
    for i in cards:
        for j in range(4):
            if i[0] == kard_suits[j]:
                suits[j] += 1
                break
        for k in range(13):
            if i[1] == kard_ranks[k]:
                ranks[k] += 1
                break

    if suits.count(5):
        ans = 'Flush'

        if straight():
            ans = 'Straight Flush'

    elif ranks.count(4):
        ans = 'Four of a Kind'

    elif ranks.count(3):
        ans = 'Three of a kind'

        if ranks.count(2):
            ans = 'Full House'

    elif straight():
        ans = 'Straight'

    elif ranks.count(2) == 2:
        ans = 'Two pair'

    elif ranks.count(2):
        ans = 'One pair'

    else:
        ans = 'High card'

    print("#{} {}".format(test_case + 1, ans))
import sys
sys.stdin = open("D3_9778_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    card = [0, 0, 4, 4, 4, 4, 4, 4, 4, 4, 16, 4]
    num = 0
    ans = "STOP"
    for _ in range(N):
        deck = int(input())
        card[deck] -= 1
        num += deck
    if sum(card[:21 - num]) > sum(card[21 - num:]):
        ans = "GAZUA"
    print("#{} {}".format(test_case + 1, ans))
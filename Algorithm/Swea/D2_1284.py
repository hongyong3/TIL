import sys
sys.stdin = open("D2_1284_input.txt", "r")

T = int(input())
for test_case in range(T):
    P, Q, R, S, W = map(int, input().split())
    cost = [0, 0]
    cost[0] = P * W
    if R >= W:
        cost[1] = Q
    else:
        cost[1] = Q + (W - R) * S
    print("#{} {}".format(test_case + 1 , min(cost)))
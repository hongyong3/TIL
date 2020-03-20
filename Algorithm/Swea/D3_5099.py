import sys
sys.stdin = open("D3_5099_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    pizza = [[y, x + 1] for x, y in enumerate(list(map(int, input().split())))]
    print(pizza)
    oven = [0] * N

    # for i in range(N):
    #     oven[i] = data.pop(0)
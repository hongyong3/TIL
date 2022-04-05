import sys
sys.stdin = open("D4_13240_input.txt", "r")

T = int(input())
for test_case in range(T):
    H, W, N = map(int, input().split())
    arr = input().split()
    wordLen = len(max(arr))
    ans = 0
    # if wordLen <= W:

    # garo, sero = float('inf'), float('inf')
    # for i in arr:
    #     minGaro = W // len(i)
    #     if minGaro < garo:
    #         garo = minGaro
    # print(garo)
    # for i in range(len(arr), - 1, - 1):
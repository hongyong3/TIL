import sys
sys.stdin = open("D3_3282_input.txt", "r")

def knapsack(n, k, data):
    ans = [[0 for x in range(K + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(K + 1):
            if i == 0 or w == 0:
                ans[i][w] = 0
            elif data[i - 1][0] <= w:
                ans[i][w] = max(data[i - 1][1] + ans[i - 1][w - data[i - 1][0]], ans[i - 1][w])
            else:
                ans[i][w] = ans[i - 1][w]
    return ans[n][k]


T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())    # N : 물건의 개수 K : 가방의 부피
    data = [list(map(int, input().split())) for _ in range(N)]  # data[i][0] : 물건의 부피 data[i][1] : 물건의 가치
    print("#{} {}".format(test_case + 1, knapsack(N, K, data)))
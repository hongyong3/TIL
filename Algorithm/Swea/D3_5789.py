import sys
sys.stdin = open("D3_5789_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, Q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(Q)]
    ans = [0] * N
    for i in range(Q):
        for j in range(data[i][0] - 1, data[i][1]):
            ans[j] = i + 1
    print("#{}".format(test_case + 1), *ans)
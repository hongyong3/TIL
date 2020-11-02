import sys
sys.stdin = open("D3_9229_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans = - 1
    data = list(map(int, input().split()))

    for i in range(N):
        for j in range(N):
            if not (i == j):
                temp = data[i] + data[j]
                if temp <= M:
                    ans = max(ans, temp)

    print("#{} {}".format(test_case + 1, ans))
import sys
sys.stdin = open("D2_9489_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        temp = 0
        for j in range(M):
            if arr[i][j]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(ans, temp)

    for j in range(M):
        temp = 0
        for i in range(N):
            if arr[i][j]:
                temp += 1
            else:
                ans = max(ans, temp)
                temp = 0
        ans = max(ans, temp)
    print("#{} {}".format(test_case + 1, ans))
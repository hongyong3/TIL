import sys
sys.stdin = open("D4_12173_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for j in range(1, M):
        arr[0][j] += arr[0][j - 1]

    for i in range(1, N):
        arr[i][0] += arr[i - 1][0]

    for i in range(1, N):
        for j in range(1, M):
            arr[i][j] += max(arr[i][j - 1], arr[i - 1][j])
    print("#{} {}".format(test_case + 1, arr[- 1][- 1]))
import sys
sys.stdin = open("4014_input.txt", "r")

# 39 / 50
def solve(arr):
    cnt = 1
    value = arr[0]
    for i in range(1, N):
        if arr[i] < value:
            if abs(value - arr[i]) > 1:
                return 0
            else:
                if i + X > N:
                    return 0
                else:
                    for j in range(i, i + X):
                        if arr[j] != arr[i]:
                            return 0
                    cnt = - X + 1

        elif arr[i] > value:
            if arr[i] - value > 1:
                return 0
            else:
                if cnt >= X:
                    cnt += 1
                else:
                    return 0
        else:
            cnt += 1
        value = arr[i]
    return 1


T = int(input())
for test_case in range(T):
    N, X = map(int, input().split())
    dataRow = [list(map(int, input().split())) for _ in range(N)]
    dataCol = [[element for element in t] for t in zip(*dataRow)]
    ans = 0

    for i in range(N):
        ans += solve(dataRow[i])
        ans += solve(dataCol[i])
    print("#{} {}".format(test_case + 1, ans))
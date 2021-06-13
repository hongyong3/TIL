import sys
sys.stdin = open("D4_12052_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr, ans, s = [], "YES", 0
    for _ in range(N):
        temp = list(input())
        s += temp.count("#")
        arr.append(temp)
    if s % 4:
        ans = "NO"
    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == "#":
                    if arr[i][j] == arr[i][j + 1] == arr[i + 1][j] == arr[i + 1][j + 1]:
                        arr[i][j] = arr[i][j + 1] = arr[i + 1][j] = arr[i + 1][j + 1] = "."
                    else:
                        ans = "NO"
                        break
            if ans == "NO":
                break

    print("#{} {}".format(test_case + 1, ans))
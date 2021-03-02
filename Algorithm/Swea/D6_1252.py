import sys
sys.stdin = open("D6_1252_input.txt", "r")

def solve(n, size):
    global ans1, ans2
    for maxSize in range(n * n, size, - 1):
        for x in range(1, S + 2 - n):
            for y in range(1, S + 2 - n):
                cnt = 0
                for i in range(n):
                    for j in range(n):
                        if arr[x + i][y + j]:
                            cnt += 1

                if cnt >= maxSize:
                    ans1 += 1
                    ans2.append(x)
                    ans2.append(y)
                    ans2.append(n)
                    erase(x, y, n)


def erase(x, y, n):
    global N
    for i in range(n):
        for j in range(n):
            if arr[x + i][y + j]:
                arr[x + i][y + j] = 0
                N -= 1


T = int(input())
for test_case in range(T):
    S = int(input())
    N = int(input())
    arr = [[0] * (S + 1) for _ in range(S + 1)]
    data = list(map(int, input().split()))
    ans1, ans2 = 0, []

    for i in range(N):
        arr[data[2 * i]][data[2 * i + 1]] = 1

    solve(3, 4)
    if N:
        solve(2, 1)
    if N:
        solve(1, 0)

    print("#{} {}".format(test_case + 1, ans1), *ans2)
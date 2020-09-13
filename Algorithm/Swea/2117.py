import sys
sys.stdin = open("2117_input.txt", "r")

def dfs(max_K):
    global answer
    for k in range(max_K, 0, -1):
        check = 0
        for i in range(N):
            for j in range(N):
                total = k * k + (k - 1) * (k - 1)
                count = 0
                for l in range(len(mat)):
                    x = mat[l][0]
                    y = mat[l][1]
                    if abs(i - x) + abs(j - y) < k:
                        total -= M
                        count += 1
                if total <= 0:
                    if answer <= count:
                        answer = count
                        check = 1
        if check == 1:
            return

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    mat, max_K, answer = [], 2 * N - 1, -float('inf')
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                mat.append([i, j])
    dfs(max_K)
    print("#{} {}".format(test_case + 1, answer))
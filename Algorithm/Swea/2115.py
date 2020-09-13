import sys
sys.stdin = open("2115_input.txt", "r")

def dfs(i, j, honey, money, n): # 수익을 구하기
    if honey > C: return 0
    if n == M: return money
    return max(dfs(i, j, honey, money, n + 1), dfs(i, j, honey + data[i][j + n], money + data[i][j + n] ** 2, n + 1))

T = int(input())
for test_case in range(1):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    worker1, worker2, mat = 0, 0, 0
    for i in range(N):  # worker1
        for j in range(N - M + 1):
            worker1 = dfs(i, j, 0, 0, 0)  # x, y, honey, money, n
            for x in range(N):  # worker2
                k = 0   # 같은 행일 때 중복방지
                if i == x:
                    k = j + M
                for y in range(k, N - M + 1):
                    worker2 = dfs(x, y, 0, 0, 0)
                    mat = max(mat, worker1 + worker2)
    print("#{} {}".format(test_case + 1, mat))
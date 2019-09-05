import sys
sys.stdin = open("2115_input.txt", "r")

def dfs(x, y, M, C):
    dx = [0, 0]     # 좌 우
    dy = [-1, 1]    # 좌 우
    for i in range()
T = int(input())
for test_case in range(T):
    N, M, C = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans, answer, worker1, worker2 = 0, 0, [], []
    for i in range(N):
        for j in range(N):
            dfs(i, j, M, C)
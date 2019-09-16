import sys
sys.stdin = open("4013_input.txt", "r")

def dfs(idx, dir):
    visited[idx] = 1

    if (idx >= 0):   # 수정 필요 무한루프
        if data[idx][6] != data[idx - 1][2] and visited[idx - 1] == 0:
            dfs(i - 1, - dir)

    if (idx < 3):
        if data[idx][2] != data[idx + 1][6] and visited[idx + 1] == 0:
            dfs(idx + 1, - dir)

    if dir == 1:
        data[idx] = [data[idx][-1]] + data[idx][:-1]

    else:
        data[idx] = data[idx][1:] + [data[idx][0]]


T = int(input())
for test_case in range(1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * 4
    for i in range(N):
        dfs(rotation[i][0] - 1, rotation[i][1])
    score = data[0][0] + data[1][0] * 2 + data[2][0] * 4 + data[3][0] * 8
    print("#{} {}".format(test_case + 1, score))
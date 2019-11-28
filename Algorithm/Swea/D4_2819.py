import sys
sys.stdin = open("D4_2819_input.txt", "r")
dx = [- 1, 1, 0, 0]
dy = [0, 0, - 1, 1]

def dfs(x, y, num, count):
    if count == 6:
        ans.add(num)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue
        dfs(nx, ny, num * 10 + data[nx][ny], count + 1)


T = int(input())
for test_case in range(T):
    data = [list(map(int, input().split())) for _ in range(4)]
    ans = set()
    for x in range(4):
        for y in range(4):
            dfs(x, y, data[x][y], 0)
    print("#{} {}".format(test_case + 1, len(ans)))
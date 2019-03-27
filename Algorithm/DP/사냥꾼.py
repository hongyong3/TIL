import sys
sys.stdin = open("사냥꾼_input.txt", "r")

def solve():
    global ans
    dx = [-1, 1, 0, 0, -1, 1, 1, -1]
    dy = [0, 0, 1, -1, 1, 1, -1, -1]
    for i in range(len(hunter)):    # 사냥군 명수만큼
        for j in range(8):          # 8 방향 검색
            x, y = hunter[i]
            while(1):
                x += dx[j]
                y += dy[j]

                if x < 0 or x >= N or y < 0 or y >= N or data[x][y] == 3:
                    break    # 벽, 바위
                if data[x][y] == 2: # 토끼
                    ans += 1

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 0 : 빈공간, 1 : 사냥군, 2 : 토끼, 3 : 바위
    hunter =[]
    ans = 0
    for i in range(N):
        for j in range(N):
            if data[i][j] == 1:
                hunter.append((i, j))
    solve()
    print("#{} {}".format(test_case+1, ans))
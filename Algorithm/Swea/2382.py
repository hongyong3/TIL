import sys
sys.stdin = open("2382_input.txt", "r")


def combination(union):
    for i in union.keys():
        ea = union[i][0]
        dir = union[i][1]
        if len(ea) > 1:
            EA = [sum(ea)]
            direction = [dir[ea.index(max(ea))]]
            union[i] = [EA, direction]
        return union


def dfs(mic):
    global ans
    dx = [0, -1, 1, 0, 0]  # 무 상 하 좌 우
    dy = [0, 0, 0, -1, 1]  # 무 상 하 좌 우
    for _ in range(M):
        union, check = {}, 0
        for i in mic.keys():
            x, y, ea, dir = i[0], i[1], mic[i][0][0], mic[i][1][0]
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:    # 벽을 만나면
                ea = ea // 2                     # 개수를 절반으로
                if dir == 1: dir = 2        # 반
                elif dir == 2: dir = 1      # 대
                elif dir == 3: dir = 4      # 방
                elif dir == 4: dir = 3      # 향

            if (nx, ny) in union:   # 이미 cell에 미생물이 존재한다면
                check = 1
                union[(nx, ny)][0].append(ea)
                union[(nx, ny)][1].append(dir)

            else:   # cell에 다른 미생물이 없다면
                union[(nx, ny)] = [[ea], [dir]]

        if check == 1:
            mic = combination(union)

        else:
            mic = union

    for i in mic.keys():
        ans += mic[i][0][0]
    return ans



T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(K)]  # x, y, ea, direction
    mic, ans = {}, 0
    for i in range(len(data)):  # dict에 data 담기
        mic[(data[i][0], data[i][1])] = [[data[i][2]], [data[i][3]]]    # key : x, y // value : ea, direction
    answer = dfs(mic)
    print("#{} {}".format(test_case + 1, answer))
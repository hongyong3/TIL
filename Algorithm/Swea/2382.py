import sys
sys.stdin = open("2382_input.txt", "r")

def combination(union):
    for key in union.keys():
        ea, dir = union[key][0], union[key][1]
        nea = [sum(ea)]
        ndir = [dir[ea.index(max(ea))]]
        union[key] = [nea, ndir]
    return union


def dfs(mic, check):
    global mat
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for _ in range(M):
        union = {}
        for key in mic.keys():
            x, y, ea, dir = key[0], key[1], mic[key][0][0], mic[key][1][0]
            nx = x + dx[dir]
            ny = y + dy[dir]

            if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:    # 약품을 만나면
                ea = ea // 2    # 미생물의 수를 절반으로 // 미생물의 수가 1마리면 소멸
                if dir == 0: dir = 1    # 반대방향
                elif dir == 1: dir = 0
                elif dir == 2: dir = 3
                elif dir == 3: dir = 2

            if (nx, ny) in union:   # cell에 다른 미생물이 있다면
                union[(nx, ny)][0].append(ea)   # 추가
                union[(nx, ny)][1].append(dir)
                check = 1   # combination 함수를 사용하려고

            else:   # cell에 다른 미생물이 없다면
                union[(nx, ny)] = [[ea], [dir]] # 추가

        if check == 1:
            mic = combination(union)

        else:
            mic = union

    for key in mic.keys():
        ans += mic[key][0][0]

    return ans


T = int(input())
for test_case in range(T):
    N, M, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(K)]
    mic, mat = {}, 0
    for i in range(len(data)):  # dict화
        mic[(data[i][0], data[i][1])] = [[data[i][2]], [data[i][3] - 1]]
    answer = dfs(mic, 0)
    print("#{} {}".format(test_case + 1, answer))

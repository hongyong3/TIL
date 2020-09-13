import sys
sys.stdin = open("5644_input.txt", "r")

dx = [0, 0, 1, 0, - 1]  # 무상우하좌
dy = [0, - 1, 0, 1, 0]

def solve(ax, ay, bx, by):
    global mat
    ac, bc = [], []

    for i in range(A):
        X, Y, C, P = AP[i]
        if abs(ax - X) + abs(ay - Y) <= C:
            ac.append((i, P))
        if abs(bx - X) + abs(by - Y) <= C:
            bc.append((i, P))

    ac.sort(key = lambda x : x[1], reverse = True)
    bc.sort(key = lambda x : x[1], reverse = True)

    temp1, temp2, a, b = 0, 0, 0, 0
    for idx, P in ac:
        a = idx
        temp1 += P
        break
    for idx, P in bc:
        if idx != a:
            temp1 += P
            break

    for idx, P in bc:
        b = idx
        temp2 += P
        break
    for idx, P in ac:
        if idx != b:
            temp2 += P
            break
    ans += max(temp1, temp2)

T = int(input())
for test_case in range(T):
    # M : 이동 시간; A : BC의 개수;
    M, A = map(int, input().split())
    # a1 : a의 이동 방향; a2 : b의 이동 방향;
    ad = list(map(int, input().split()))
    bd = list(map(int, input().split()))
    # (X, Y) : 좌표; C : 충전 범위; P : 처리량;
    AP = [list(map(int, input().split())) for _ in range(A)]
    Ax, Ay = 1, 1
    Bx, By = 10, 10
    mat = 0
    solve(Ax, Ay, Bx, By)
    for i in range(M):
        Ax, Ay = Ax + dx[ad[i]], Ay + dy[ad[i]]
        Bx, By = Bx + dx[bd[i]], By + dy[bd[i]]
        solve(Ax, Ay, Bx, By)
    print("#{} {}".format(test_case + 1, mat))
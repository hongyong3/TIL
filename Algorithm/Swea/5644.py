import sys
sys.stdin = open("5644_input.txt", "r")

dy = [0, - 1, 0, 1, 0]  # 무상우하좌
dx = [0, 0, - 1, 0, 1]

def solve(ax, ay, bx, by):
    global ans
    ac = []
    bc = []

    for i in range(A):
        X, Y, C, P = AP[i]
        if abs(ax - X) + abs(ay - Y) <= C:
            ac.append((i, P))
        if abs(bx - X) + abs(by - Y) <= C:
            bc.append((i, P))

    ac.sort(key = lambda x : x[1], reverse = True)
    bc.sort(key = lambda x : x[1], reverse = True)

    temp1 = 0
    uu1 = 0
    for idx, P in ac:
        uu1 = idx
        temp1 += P
        break
    for idx, P in bc:
        if idx != uu1:
            temp1 += P
            break

    temp2 = 0
    uu2 = 0
    for idx, P in bc:
        uu2 = idx
        temp2 += P
        break
    for idx, P in ac:
        if idx != uu2:
            temp2 += P
            break

    ans += max(temp1, temp2)

T = int(input())
for test_case in range(T):
    # M : 이동 시간; A : BC의 개수;
    M, A = map(int, input().split())
    # a1 : a의 이동 방향; a2 : b의 이동 방향;
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    # (X, Y) : 좌표; C : 충전 범위; P : 처리량;
    AP = [list(map(int, input().split())) for _ in range(A)]

    Ax, Ay = 1, 1
    Bx, By = 10, 10
    ans = 0
    solve(Ax, Ay, Bx, By)
    for i in range(M):
        Ax, Ay = Ax + dx[a1[i]], Ay + dy[a1[i]]
        Bx, By = Bx + dx[a2[i]], By + dy[a2[i]]
        solve(Ax, Ay, Bx, By)
    print(ans)
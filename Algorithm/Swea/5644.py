import sys
sys.stdin = open("5644_input.txt", "r")

dx = [0, - 1, 0, 1, 0]  # 무상우하좌
dy = [0, 0, - 1, 0, 1]

def solve(ax, ay, bx, by):
    ac = []
    bc = []

    for i in range(A):
        X, Y, C, P = AP[i]
        if abs(ax - X) + abs(ay - Y) <= C:
            ac.append((i, P))
        if abs(bx - X) + abs(by - Y) <= C:
            bc.append((i, P))

T = int(input())
for test_case in range(T):
    # M : 이동 시간; A : BC의 개수;
    M, A = map(int, input().split())
    # a1 : a의 이동 방향; a2 : b의 이동 방향;
    a1 = list(map(int, input().split()))
    a2 = list(map(int, input().split()))
    # (X, Y) : 좌표; C : 충전 범위; P : 처리량;
    AP = [list(map(int, input().split())) for _ in range(A)]
    arr = [[0] * 10 for _ in range(10)]

    Ax, Ay = 1, 1
    Bx, By = 10, 10
    for i in range(M):
        Ax, Ay = Ax + dx[a1[i]], Ay + dy[a1[i]]
        Bx, By = Bx + dx[a2[i]], By + dy[a2[i]]

import sys
sys.stdin = open("D4_3812_input.txt", "r")

def solve(idx, offset, criteria):
    ans = 0
    quotient = (offset - criteria) // N # 몫; 몫을 구해서 몇 번 반복되는지 찾기 위함.
    remain =  (offset - criteria) % N   # 나머지; 반복되지 않는 경우를 처리하기 위함.

    for i in range(N):
        ans += color[idx - 1][i]

    for i in range(N):
        color[idx][i] = (ans * quotient) + color[idx - 1][i]

    for i in range(1, remain + 1):
        for j in range(N):
            color[idx][(i + j) % N] += color[idx - 1][j]

    quotient = criteria // N
    remain = criteria % N

    for i in range(N):
        color[idx][i] += (ans * quotient)

    for i in range(1, remain + 1):
        for j in range(N):
            color[idx][(i + j) % N] += color[idx - 1][j]

T = int(input())
for test_case in range(T):
    X, Y, Z, A, B, C, N = map(int, input().split())

    color = [[0] * N for _ in range(3)]
    for i in range(A, X):
        color[0][(i - A) % N] += 1  # A -> X 까지의 큐브의 색상 개수

    for i in range(A - 1, - 1, - 1):
        color[0][(A - i) % N] += 1  # 0 -> A - 1 큐브의 색상 개수

    solve(1, Y - 1, B)
    solve(2, Z - 1, C)
    print("#{}".format(test_case + 1), *color[2])
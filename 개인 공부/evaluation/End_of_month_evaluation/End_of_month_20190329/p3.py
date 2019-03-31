import sys
sys.stdin = open('p3.txt')


def perm(n, k, sums):
    global result

    if sums > result:
        return

    if k >= n and result > sums:
        result = sums

    for i in range(n):
        if not chk[i]:
            chk[i] = k+1
            perm(n, k+1, sums + data[k][i])
            chk[i] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    raw_cookie = list(map(int, input().split()))
    raw_robots = list(map(int, input().split()))

    cookie = [(raw_cookie[_], raw_cookie[_+1]) for _ in range(0, 2*N, 2)]
    robots = [(raw_robots[_], raw_robots[_ + 1]) for _ in range(0, 2 * N, 2)]

    data = [[0 for _ in range(N)] for _ in range(N)]

    for idx1 in range(N):
        for idx2 in range(N):
            data[idx1][idx2] = abs(cookie[idx1][0] - robots[idx2][0]) + abs(cookie[idx1][1] - robots[idx2][1])

    chk = [0 for _ in range(N)]
    result = float('inf')
    perm(N, 0, 0)
    print('#{} {}'.format(tc, result))

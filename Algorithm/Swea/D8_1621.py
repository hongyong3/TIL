import sys
sys.stdin = open("D8_1621_input.txt", "r")

def solve(c):
    t = 0
    for i in range(N):
        t += dist[i] / (speed[i] + c)
    return t

T = int(input())
for test_case in range(T):
    N, T = map(int, input().split())
    dist, speed = [0] * N, [0] * N
    for i in range(N):
        dist[i], speed[i] = map(int, input().split())

    low = - min(speed) + pow(10, - 9)
    high = 10000000

    for _ in range(10000):
        mid = (low + high) / 2
        f = solve(mid)
        if f > T:
            low = mid
        else:
            high = mid
    print("#{} {}".format(test_case + 1, low))
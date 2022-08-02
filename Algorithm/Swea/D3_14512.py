import sys
sys.stdin = open("D3_14512_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    # arr = [list(map(int, input().split())) for _ in range(N)]
    time = [0] * M
    print("#{} {} {}".format(test_case + 1, N, M))
    for _ in range(N):
        s, e = map(int, input().split())
        for t in range(s - 1, e):
            time[t] += 1
    print(time)

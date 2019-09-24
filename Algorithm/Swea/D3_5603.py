import sys
sys.stdin = open("D3_5603_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    avg, count = 0, 0
    for i in range(N):
        avg += data[i][0]
    avg = avg // N
    for i in range(N):
        count += abs(avg - data[i][0])
    print("#{} {}".format(test_case + 1, count // 2))
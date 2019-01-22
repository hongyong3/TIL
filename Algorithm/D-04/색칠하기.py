import sys
sys.stdin = open("색칠하기_input.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    data = [[0 for _ in range(10)] for _ in range(10)]
    for i in range(N):
        count = 0
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, (r2+1)):
            for j in range(c1, (c2+1)):
                data[i][j] += color
                if data[i][j] == 3:
                    count += 1

    print(f"#{test_case} {count}")
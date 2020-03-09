import sys
sys.stdin = open("D2_4836_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [[0] * (10) for _ in range(10)]
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                data[i][j] += color
                # if data[i][j] == 3:
                #     count += 1
    for i in data:
        count += i.count(3)
    print("#{} {}".format(test_case + 1, count))
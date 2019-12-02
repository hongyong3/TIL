import sys
sys.stdin = open("sum_input.txt")

T = 10
for test_case in range(T):
    N = int(input())
    data = [[0 for _ in range(100)] for _ in range(100)]
    for i in range(100):
        data[i] = list(map(int, input().split()))
    sum = []

    for x in range(len(data)):
        line_m = 0
        for y in range(len(data[0])):
            line_m += data[x][y]
        sum.append(line_m)
    for y in range(len(data)):
        line_n = 0
        for x in range(len(data[0])):
            line_n += data[x][y]
        sum.append(line_n)

    for x in range(len(data)):
        line_mn = 0
        for y in range(len(data[0])):
            if x == y:
                line_mn += data[x][y]
            sum.append(line_mn)
            if x + y == len(data) - 1:
                line_mn += data[x][y]
            sum.append(line_mn)

    for x in range(len(data)):
        line_nm = 0
        for y in range(len(data[0])):
            line_nm += data[x][99 - y]
            sum.append(line_mn)
    sum.sort()
    print("#{} {}".format(test_case+1, sum[-1]))
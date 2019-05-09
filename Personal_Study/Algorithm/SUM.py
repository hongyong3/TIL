import sys
sys.stdin = open("SUM_inut.txt", "r")
for test_case in range(10):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(100)]
    sum = []
    line_mn, line_nm = 0, 0
    for x in range(len(data)):
        line_mn += data[x][x]
        line_nm += data[x][99 - x]
    sum.append(line_mn)
    sum.append(line_nm)

    for x in range(len(data)):
        line_m, line_n = 0, 0
        for y in range(len(data[0])):
            line_m += data[x][y]
            line_n += data[y][x]
        sum.append(line_n)
        sum.append(line_m)

    print("#{} {}".format(test_case + 1, min(sum)))
    print("#{} {}".format(test_case + 1, max(sum)))
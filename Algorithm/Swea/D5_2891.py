import sys
sys.stdin = open("D5_2891_input.txt", "r")

num = '123456789'
T = int(input())
for test_case in range(1):
    garo = [[0] * 10 for _ in range(7)]
    garoNum = [[0] * 10 for _ in range(7)]
    sero = [[[0] * 10 for _ in range(7)] for _ in range(2)]
    for i in range(1, 7):
        data = list(map(str, input().split()))
        print(*data)
        k = 1
        for j in range(6):
            if len(data[j]) == 3:
                if data[j][0] == '-':
                    k += 1
                else:
                    garo[i][k] = 1
                    garoNum[i][int(data[j][0])] = 1
                    k += 1
                if data[j][2] == '-':
                    k += 1
                else:
                    garo[i][k] = 1
                    garoNum[i][int(data[j][2])] = 1
                    k += 1
            else:
                if data[j] == '-':
                    k += 1
                else:
                    garo[i][k] = 1
                    garoNum[i][int(data[j])] = 1
                    k += 1
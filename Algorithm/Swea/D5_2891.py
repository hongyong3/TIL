import sys
sys.stdin = open("D5_2891_input.txt", "r")

num = '123456789'
T = int(input())
for test_case in range(1):
    garo = [[0] * 10 for _ in range(7)]
    garoNum = [[0] * 10 for _ in range(7)]
    sero = [[0] * 10 for _ in range(7)]
    seroNum = [[0] * 10 for _ in range(7)]
    box = []
    arr = []
    for i in range(1, 7):
        data = list(map(str, input().split()))
        arr.append(data)
        k = 1
        for j in range(6):
            if len(data[j]) == 3:   # 분수이면
                if data[j][0] == '-':   # 분자에 숫자가 없다면
                    k += 1
                else:   # 분자에 숫자가 있다면
                    garo[i][k] = 1  # 가로열의 해당 칸 check
                    garoNum[i][int(data[j][0])] = 1 # 가로열에 들어있는 숫자 추가
                    k += 1
                if data[j][2] == '-':   # 분모에 숫자가 없다면
                    k += 1
                else:   # 분모에 숫자가 있다면
                    garo[i][k] = 1  # 가로열의 해당 칸 check
                    garoNum[i][int(data[j][2])] = 1 # 가로열에 들어있는 숫자 추가
                    k += 1
            else:   # 정수라면
                if data[j] == '-':  # 숫자가 없다면
                    k += 1
                else:   # 숫자가 있다면
                    garo[i][k] = 1  # 가로열의 해당 칸 check
                    garoNum[i][int(data[j])] = 1    # 가로열에 들어있는 숫자 추가
                    k += 1

    for idx, i in enumerate(zip(*arr)):
        k = 1
        for j in range(6):
            if len(i[j]) == 3:
                if i[j][0] == '-':
                    k += 1
                else:
                    sero[idx + 1][k] = 1
                    seroNum[idx + 1][int(i[j][0])] = 1
                    k += 1
                if i[j][2] == '-':
                    k += 1
                else:
                    sero[idx + 1][k] = 1
                    seroNum[idx + 1][int(i[j][2])] = 1
                    k += 1
            else:
                if i[j] == '-':
                    k += 1
                else:
                    sero[idx + 1][k] = 1
                    seroNum[idx + 1][int(i[j])] = 1
                    k += 1

    # box...
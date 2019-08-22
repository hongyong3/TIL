import sys
sys.stdin = open("D3_4751_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = list(str(input()))
    count = 4 * len(data) + 1
    temp = [['.'] * count for _ in range(5)]

    for i in range(5):
        for j in range(len(data)):
            if i == 0 or i == 4 :
                temp[i][2 + 4 * j] = "#"
            elif i == 1 or i == 3:
                temp[i][1 + 4 * j] = "#"
                temp[i][3 + 4 * j] = "#"
            else:
                temp[i][4 * j] = "#"
    temp[2][-1] = "#"
    for i in range(len(data)):
        temp[2][2 + 4 * i] = data[i]
    for i in temp:
        print("".join(i))
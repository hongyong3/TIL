import sys
sys.stdin = open("빙고_input.txt", "r")
data = [list(map(int, input().split())) for _ in range(5)]
answer = [list(map(int, input().split())) for _ in range(5)]

def find(num):
    for i in range(5):
        for j in range(5):
            if data[i][j] == num:
                data[i][j] = 0
                return

def Bingo():
    Crosum1, Crosum2 = 0, 0
    count = 0
    for i in range(5):
        Rsum, Csum = 0, 0
        for j in range(5):
            Rsum += data[i][j]
            Csum += data[j][i]
        if Rsum == 0:
            count += 1
        if Csum == 0:
            count += 1
        Crosum1 += data[i][i]
        Crosum2 += data[i][4 - i]

    if Crosum1 == 0:
        count += 1
    if Crosum2 == 0:
        count += 1
    if count >= 3:
        return True
    else:
        return False

flag = 0
for i in range(5):
    for j in range(5):
        find(answer[i][j])
        if Bingo() == True:
            flag = 1
            break
    if flag == 1:
        break
print(i * 5 + j + 1)
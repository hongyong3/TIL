import sys
sys.stdin = open("4013_input.txt", "r")

T = int(input())
for test_case in range(1):
    K = int(input())
    data = [list(map(int, input().split())) for _ in range(4)]
    rotation = [list(map(int, input().split())) for _ in range(K)]

    ans, sum = 0, 0

    for i in range(K):
        if rotation[i][1] == 1:   # 시계방향
            ans = data[rotation[i][0] - 1].pop(0)
            data[rotation[i][0] - 1].append(ans)
            
        else:   # 반시계방향
            pass
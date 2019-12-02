import sys
sys.stdin = open('농작물 수확하기1_input.txt', "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    sum = 0
    for i in range(N):
        if i == 0 or i == N-1:
            sum += data[i][N//2]
        elif 0 < i < N//2:
            sum += data[i][N//2]
            j = 1
            while j < i+1:
                sum += data[i][N//2-j]
                sum += data[i][N//2+j]
                j += 1
        else:
            sum += data[i][N//2]
            j = 1
            while j < N -i:
                sum += data[i][N//2-j]
                sum += data[i][N//2+j]
                j += 1
    print("#{} {}".format(test_case+1, sum))
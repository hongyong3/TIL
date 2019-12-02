import sys
sys.stdin = open('X_SUM_input.txt', "r")
T = int(input())
for test_case in range(T):
    N, K = list(map(int,input().split()))
    data = [list(map(int,input().split())) for _ in range(N)]

    substract = []
    min = 987654

    for i in range(N-K+1):
        for j in range(N-K+1):
            cross_left = 0
            cross_right = 0
            for s in range(K):
                    cross_right += data[i+s][j+s]
                    cross_left += data[i+s][K+j-1-s]
                    if cross_right > cross_left:
                        substract.append(cross_right-cross_left)
                    else:
                        substract.append(cross_left-cross_right)


    for i in substract:
        if i < min:
            min = i

    print(min)
import sys
sys.stdin = open("D4_3349_input.txt", "r")

T = int(input())
for test_case in range(T):
    W, H, N = map(int, input().split())
    xy = [list(map(int, input().split())) for _ in range(N)]
    count = 0
    for i in range(N - 1):
        X, Y = xy[i + 1][0] - xy[i][0], xy[i + 1][1] - xy[i][1]
        if X *  Y > 0:
            if abs(X) > abs(Y):
                count += abs(Y) + (abs(X) - abs(Y))
            else:
                count += abs(X) + (abs(Y) - abs(X))
        else:
            count += abs(X) + abs(Y)
    print("#{} {}".format(test_case + 1, count))
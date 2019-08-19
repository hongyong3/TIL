import sys
sys.stdin = open("D3_5789_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, Q = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(Q)]
    temp = [0] * N
    k = 0
    for i in range(Q):
        k += 1
        for j in range(data[i][0] - 1, data[i][1]):
            temp[j] = k
    print("#{} ".format(test_case + 1), end="")
    print(*temp)
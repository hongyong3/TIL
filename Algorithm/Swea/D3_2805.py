import sys
sys.stdin = open("D3_2805_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input())) for _ in range(N)]
    j, mat = - 1, 0
    for i in range(N):
        if i <= N // 2: j += 1
        else: j -= 1
        mat += (sum(data[i][(N // 2) - j: (N // 2) + j + 1]))
    print("#{} {}".format(test_case + 1, mat))
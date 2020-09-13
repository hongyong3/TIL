import sys
sys.stdin = open("D3_6692_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(float, input().split())) for _ in range(N)]
    mat = 0
    for i in range(N):
        mat += data[i][0] * data[i][1]
    print("#{} {}".format(test_case + 1, format(mat, "6f")))

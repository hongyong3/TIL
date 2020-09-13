import sys
sys.stdin = open("D4_3820_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    data = sorted(data, key=lambda x: (-(x[0] - 1) / x[1]))
    mat = 1
    for a, b in data:
        mat = (mat * a + b) % 1000000007
    print("#{} {}".format(test_case + 1, mat))
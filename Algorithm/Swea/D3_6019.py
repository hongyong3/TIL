import sys
sys.stdin = open("D3_6019_input.txt", "r")

T = int(input())
for test_case in range(T):
    D, A, B, F = map(float, input().split())
    time = D / (A + B)
    mat = F * time
    print("#{} {}".format(test_case + 1, format(float(mat), ".10f")))
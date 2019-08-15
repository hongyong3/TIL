import sys
sys.stdin = open("D3_6019_input.txt", "r")

T = int(input())
for test_case in range(T):
    D, A, B, F = map(float, input().split())
    ans = D / float(A + B)
    print("#{} {}".format(test_case + 1, float(ans)))
    # print("#{} {}".format(test_case + 1, format(ans, "6f")))
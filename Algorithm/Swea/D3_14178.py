import sys
sys.stdin = open("D3_14178_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, D = map(int, input().split())
    ans = N / (2 * D + 1)
    ans = int(ans) if ans == int(ans) else int(ans) + 1
    print("#{} {}".format(test_case + 1, ans))
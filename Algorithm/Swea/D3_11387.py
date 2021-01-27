import sys
sys.stdin = open("D3_11387_input.txt", "r")

T = int(input())
for test_case in range(T):
    D, L, N = map(int, input().split())
    ans = 0
    for i in range(N):
        ans += D * (1 + i * L * 0.01)
    print("#{} {}".format(test_case + 1, int(ans)))
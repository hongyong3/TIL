import sys
sys.stdin = open("D2_15088_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(set((map(int, input().split())))))
    ans = 0
    for i in range(N - 1):
        val1, val2 = arr[i], arr[i + 1]
        ans = max(ans, (val2 - val1) >> 1)
    print(ans)
import sys
sys.stdin = open("D4_18799_input.txt", "r")

from itertools import combinations
T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    avg = 0
    for i in range(1, N + 1):
        tot = list(combinations(arr, i))
        for j in tot:
            avg += sum(j) / i
    ans = avg / (2 ** N - 1)
    if ans == int(ans):
        ans = int(ans)
    print("#{} {}".format(test_case + 1, ans))
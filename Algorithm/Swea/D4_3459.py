import sys
sys.stdin = open("D4_3459_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = "Alice"
    while N >= 10:
        N = (N // 2) + 1
        N = (N // 2) - 1
    if N == 1 or (6 <= N <= 9):
        ans = "Bob"
    print("#{} {}".format(test_case + 1, ans))
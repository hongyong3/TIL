import sys
sys.stdin = open("D4_6026_input.txt", "r")
def factorial(n):
    if n == 1 :
        return 1
    else:
        return n * factorial(n-1)
T = int(input())
for test_case in range(T):
    M, N = map(int, input().split())
    ans = 0
    if M == N:
        ans = factorial(M)
    else:
        ans = M ** N - factorial(M)
    print("#{} {}".format(test_case + 1, ans % 1000000007))
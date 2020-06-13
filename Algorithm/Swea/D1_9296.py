import sys
sys.stdin = open("D1_9296_input.txt", "r")

def fib(n):
    if n == 1:
        return 1
    for i in range(2, n + 1):
        memo.append(memo[i - 1] + memo[i - 2])
    return memo[n]

for i in range(5):
    memo = [0, 1]
    n = int(input())
    print(fib(n))
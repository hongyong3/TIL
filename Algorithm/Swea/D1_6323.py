import sys
sys.stdin = open("D1_6323_input.txt", "r")

def fib(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fib(n - 1) + fib(n - 2))
    return memo[n]

memo = [0, 1]
fib(int(input()))
print(memo[1:])
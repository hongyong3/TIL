def fib(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fib(n - 2) + fib(n - 1))
    return memo[n]

memo = [0, 1]
fib(10)
print(memo[1:])
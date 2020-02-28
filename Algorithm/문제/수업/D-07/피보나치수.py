def fib(n):
    if n < 2:
        return n
    else:
        return fib(n - 1) + fib(n - 2)

memo = [0, 1]
print(fib(8))
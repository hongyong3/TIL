'''
memo를 위한 배열을 할당하고, 모두 0으로 초기화 한다.
momo[0]을 0으로 momo[1]은 1로 초기화 한다.
'''
def fib(n):
    global memo
    if n >=2 and len(memo) <= n:
        memo.append(fib(n-1) + fib(n-2))
    return memo[n]

memo = [0, 1]
print(fib(998))
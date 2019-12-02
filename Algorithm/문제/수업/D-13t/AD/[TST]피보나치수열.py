import sys
sys.stdin = open("[TST]피보나치수열_input.txt", "r")

def fibonacci(N):
    a, b = 1, 0
    for i in range(N):
        a, b = b, a + b
    return b

N = int(input())
print(fibonacci(N))
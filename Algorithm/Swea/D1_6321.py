import sys
sys.stdin = open("D1_6321_input.txt", "r")

def prime(n):
    m = int(pow(n, 0.5))
    sieve = [1] * n
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(2 * i, n, i):
                sieve[j] = 0
    if sieve[- 1]:
        return "소수입니다."

print(prime(int(input()) + 1))
def prime_list_N(x):
    sieve = [True] * x  # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    n = int(x ** 0.5)   # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, n + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, x, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(2, x) if sieve[i] == True] # 소수 목록 산출

def prime_list_M(y):
    sieve = [True] * y  # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    m = int(y ** 0.5)   # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, y, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False
    return [i for i in range(2, y) if sieve[i] == True] # 소수 목록 산출

import sys
sys.stdin = open("소수의 개수와 최대 최소 구하기_input.txt", "r")
N, M = list(map(int, input().split()))
A, B = min(N, M), max(N, M)
prime_list_N(N)
prime_list_M(M)
count = 0
X = set(prime_list_M(M)) - set(prime_list_N(N))
print(len(X))
print(min(X)+max(X))
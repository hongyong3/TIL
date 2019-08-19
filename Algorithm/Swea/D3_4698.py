import sys
sys.stdin = open("D3_4698_input.txt", "r")

def getPrimeList(N):
    sieve = [True] * N
    m = int(N ** (1 / 2))
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False
    return [i for i in range(2, N) if sieve[i]]

T = int(input())
prime_list = getPrimeList(10 ** 6)
for test_case in range(T):
    D, A, B = map(int, input().split())
    count = 0
    for i in prime_list:
        if A <= i <= B and str(D) in str(i): count += 1
        if i > B: break
    print("#{} {}".format(test_case + 1, count))
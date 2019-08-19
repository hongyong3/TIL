import sys
sys.stdin = open("D3_5986_input.txt", "r")

def getPrimeList(N):
    sieve = [True] * N
    m = int(N ** (1 / 2))
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False
    return [i for i in range(2, N) if sieve[i]]

T = int(input())
for test_case in range(T):
    N = int(input())
    answer = []
    prime_list = getPrimeList(N)

    for x in prime_list[::-1]:
        for y in prime_list:
            if x >= y:
                z = N - x - y
                if z in prime_list and y >= z:
                    answer.append([x, y, z])
            else:
                break
    print("#{} {}".format(test_case + 1, len(answer)))
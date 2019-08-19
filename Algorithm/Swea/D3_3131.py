def getPrimeList(N):
    sieve = [True] * N
    m = int(N ** (1 / 2))
    for i in range(2, m + 1):
        if sieve[i]:
            for j in range(i + i, N, i):
                sieve[j] = False
    return [i for i in range(2, N) if sieve[i]]

print(*getPrimeList(10**6))
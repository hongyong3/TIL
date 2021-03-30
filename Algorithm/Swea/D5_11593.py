import sys
sys.stdin = open("D5_11593_input.txt", "r")


# multiset permutation?
fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]

T = int(input())
for test_case in range(T):
    s = list(input())
    alpha = [0] * 26
    for i in s:
        alpha[ord(i) - 65] += 1

    ans = 0
    idx, k = 0, len(s)

    while k:
        for i in range(26):
            if alpha[i]:
                if ord(s[idx]) - 65 > alpha[i]:
                    temp = fact[k - 1]
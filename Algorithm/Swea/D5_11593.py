import sys
sys.stdin = open("D5_11593_input.txt", "r")

'''
from collections import Counter as Multiset


def multiset_combinations(ms, n):
    assert sum(ms.values()) >= n
    def f(ms_res, curr_val, ms_rem):
        nonlocal n
        if sum(ms_res.values()) == n:  #ideally len would return the number of total elements
            yield ms_res
        else:
            for val in set(ms_rem):
                if val >= curr_val:
                    # for each unique value in remaining multiset equal to or larger than the current value
                    val_ms = Multiset((val,))  # ideally I wouldn't need to wrap a singleton multiset
                    # add that value to the result multiset and remove it from remaining multiset
                    yield from f(ms_res + val_ms, val, ms_rem - val_ms)
                    # recurse
    yield from f(Multiset(), sorted(ms.keys())[0], ms)

for m in multiset_combinations(Multiset((3, 3, 4, 4, 4, 5)), 3):
    print(list(m.elements()))
'''


# multiset permutation?
# fact = [0, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800, 39916800, 479001600, 6227020800, 87178291200, 1307674368000, 20922789888000, 355687428096000, 6402373705728000, 121645100408832000, 2432902008176640000]
#
# T = int(input())
# for test_case in range(T):
#     s = list(input())
#     alpha = [0] * 26
#     for i in s:
#         alpha[ord(i) - 65] += 1
#
#     ans = 0
#     idx, k = 0, len(s)
#
#     while k:
#         for i in range(26):
#             if alpha[i]:
#                 if ord(s[idx]) - 65 > alpha[i]:
#                     temp = fact[k - 1]

fact = [1]
idx = 1
for i in range(1, 21):
    fact.append(fact[i - 1] * idx)
    idx += 1

T = int(input())
for test_case in range(T):
    s = input()
    n = len(s)
    alpha = [0] * 26
    ans = 0
    for i in s:
        alpha[ord(i) - 65] += 1

    for i in range(n):
        c = ord(s[i]) - 65
        for j in range(c):
            if alpha[j]:
                temp = fact[n - 1 - i]
                alpha[j] -= 1
                for k in range(26):
                    temp //= fact[alpha[k]]
                ans += temp
                alpha[j] += 1
        alpha[c] -= 1
    print("#{} {}".format(test_case + 1, ans))
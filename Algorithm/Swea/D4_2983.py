import sys
sys.stdin = open("D4_2983_input.txt", "r")

# Runtime Error 7 // 10
from collections import defaultdict
def kasai(s, sa):
    k = 0

    for i in range(N):
        rank[sa[i]] = i

    for i in range(N):
        if rank[i] == N - 1:
            k = 0
            continue
        j = sa[rank[i] + 1]
        while j + k < N and i + k < N and s[i + k] == s[j + k]:
            k += 1
        lcp[rank[i]] = k
        k = max(0, k - 1)
    return lcp

def manber_myers(s, buckets, t):
    g = defaultdict(list)   # group
    for bucket in buckets:
        g[s[bucket:bucket + t]].append(bucket)
    arr = []
    for k, v in sorted(g.items()):
        if len(v) > 1:
            arr.extend(manber_myers(s, v, t * 2))
        else:
            arr.append(v[0])
    return arr

T = int(input())
lcp = [0] * 200001
rank = [0] * 200001
for test_case in range(T):
    N = int(input())
    S = input()

    for i in range(N):
        rank[i], lcp[i] = 0, 0

    SA = manber_myers(S, range(N), 1)
    kasai(S, SA)
    print("#{} {}".format(test_case + 1, max(lcp[:N])))
    
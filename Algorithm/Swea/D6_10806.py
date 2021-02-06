import sys
sys.stdin = open("D6_10806_input.txt", "r")

import heapq
T = int(input())
for test_case in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    K = int(input())
    h = []
    heapq.heappush(h, (0, K))

    while h[0][1]:
        x, y = heapq.heappop(h)
        heapq.heappush(h, (x + y, 0))
        for i in range(N):
            heapq.heappush(h, (x + y % A[i], y // A[i]))
    print("#{} {}".format(test_case + 1, h[0][0]))
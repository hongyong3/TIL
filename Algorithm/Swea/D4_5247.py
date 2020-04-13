import sys
sys.stdin = open("D4_5247_input.txt", "r")

from collections import deque
def bfs(n):
    q = deque([[n, 0]])
    while q:
        num, count = q[0]
        if num > M + 11:
            q.popleft()
            continue
        flag = 1
        temp = []
        temp.append(num + 1)
        temp.append(num * 2)
        temp.append(num - 1)
        temp.append(num - 10)
        count += 1
        for i in temp:
            if 0 <= i < M + 11 and counts[i] > count:
                counts[i] = count
                flag = 0
                q.append([i, count])
        if flag:
            q.popleft()

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    counts = [float('inf')] * (M + 11)
    bfs(N)
    print("#{} {}".format(test_case + 1, counts[M]))
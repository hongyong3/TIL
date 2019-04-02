import time
from time import strftime
start_time = time.time()
import sys
sys.stdin = open("사람 네트워크2_input.txt", "r")

# 선생님 풀이
T = int(input())
for test_case in range(T):
    temp = list(map(int, input().split()))

    N = temp.pop(0)
    adj = [[0]*N for _ in range(N)]
    idx = 0
    for i in range(N):
        for j in range(N):
            adj[i][j] = temp[idx]
            if i != j and adj[i][j] == 0:   # 0인 가중치를 무한대로
                adj[i][j] = 9876543210
            idx += 1

    for k in range(N):
        for i in range(N):
            if i == k: continue
            for j in range(i+1, N, 1):
                if j == k or i == j: continue
                if adj[i][j] > adj[i][k] + adj[k][j]:
                    adj[j][i] = adj[i][j] = adj[i][k] + adj[k][j]

    minV = 9876543210
    for i in range(N):
        sum = 0
        for j in range(N):
            sum += adj[i][j]
        if sum < minV:
            minV = sum

    print("#{} {}".format(test_case+1, minV))
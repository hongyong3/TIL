import time
from time import strftime
start_time = time.time()
import sys
sys.stdin = open("연산_input.txt", "r")

def BFS(N, count):
    Q = [(N, count)]
    visited[N] = 1
    while Q:
        N, count = Q.pop(0)
        operation = [N+1, N-1, N*2, N-10]
        if N == M:
            return count
        for i in range(4):
            NN = operation[i]
            if NN < 0 or NN > 1000000: continue
            if visited[NN] == 0:
                visited[NN] = 1
                Q.append((NN, count+1))

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    visited = [0] * 1000001
    print("#{} {}".format(test_case+1, BFS(N, 0)))
print(time.time() - start_time, 'seconds')
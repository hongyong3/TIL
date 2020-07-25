import sys
sys.stdin = open("D5_3308_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    visited = [0] * (N + 1)
    for i in range(1, N - 1):
        for j in range(2, N):
            if data[i] < data[j]:
                visited[i] = visited[0] + visited[i] + 1
    print(visited)
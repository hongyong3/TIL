import sys
sys.stdin = open("D3_9829_input.txt", "r")

def solve(n):
    global visited
    for idx, val in enumerate(data):
        if val == n:
            if visited[idx]:
                pass
            else:
                visited[idx] = 1

T = int(input())
for test_case in range(T):
    L, S = map(int, input().split())
    visited = [0] * L

    for i in range(S):
        data = list(map(int, input().split()))
        if data.count(0) < data.count(1):
            solve(0)
        else:
            solve(1)
    print("#{} {}".format(test_case + 1, visited.index(0) + 1))
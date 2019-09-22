import sys
sys.stdin = open("Line_test3_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    visited = [0] * 151
    for i in range(N):
        data = list(map(int, input().split()))
        for i in range(data[0], data[1]):
            visited[i] += 1
    print(max(visited))
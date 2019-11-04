import sys
sys.stdin = open("D4_3752_input.txt", "r")
T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    visited, total = [0 for _ in range(10001)], 0
    for i in range(N):
        total += data[i]
        for j in range(total, -1, -1):
            if visited[j]:
                visited[j + data[i]] = 1
        visited[data[i]] = 1
    print("#{} {}".format(test_case + 1, sum(visited) + 1))
import sys
sys.stdin = open("D5_9232_input.txt", "r")

def solve(x):
    global visited
    if len(disk) == 0:
        return
    if visited[0] == 1:
        visited = [0]
        return
    y = disk.pop(0)
    while data[x + 1] >= y:
        if not visited[x + 1]:
            x += 1
        else:
            break
    visited[x] = 1
    solve(- 1)


T = int(input())
for test_case in range(T):
    N, Q = map(int, input().split())
    data = list(map(int, input().split()))
    disk = list(map(int, input().split()))
    mat = 0
    visited = [0 for _ in range(N)]

    solve(- 1)
    for i in range(len(visited)):
        if len(visited) == 1:
            mat = 0
            break
        elif visited[i] == 1:
            mat = i + 1
            break
    print("#{} {}".format(test_case + 1, mat))
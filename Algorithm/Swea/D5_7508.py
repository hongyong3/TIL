import sys
sys.stdin = open("D5_7508_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    A = sorted(list(map(int, input().split())))
    M = int(input())
    W = sorted(list(map(int, input().split())))
    visited = [0] * N
    idx = 0
    for i in W:
        while i > A[idx]:
            idx += 1
            if idx == len(A):
                break
        if idx == len(A):
            break
        visited[idx] += 1

    if sum(visited) < len(W):
        mat = - 1
    else:
        mat, idx, work = 0, 0, 0
        visited.reverse()
        for i in range(len(visited)):
            visited[i] -= work
            work = 0
            if visited[i] > 0:
                idx += 1
                if visited[i] % idx == 0:
                    temp = visited[i] // idx
                    mat += temp
                    visited = list(map(lambda x : x - temp, visited))
                    work = 0
                else:
                    temp = visited[i] // idx + 1
                    mat += temp
                    work = idx - visited[i] % idx
                    visited = list(map(lambda x : x - temp, visited))

            elif visited[i] < 0:
                work = - visited[i]
                idx += 1

            else:
                idx += 1
    print("#{} {}".format(test_case + 1, mat))
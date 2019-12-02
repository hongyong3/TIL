#import sys
#sys.stdin = open("작업순서_input.txt")

for test_case in range(10):
    V, E = map(int, input().split())
    # print(V, E)
    G = [[0 for _ in range(V)] for _ in range(V)]
    # print(G)
    visited = list(range(V))
    # print(visited)
    answer = []

    data = list(map(int, input().split()))
    for i in range(0, E * 2 - 1, 2):
        a, b = data[i], data[i + 1]
        G[a - 1][b - 1] = 1

    while visited:

        for j in visited:
            for row in G:
                if row[j] == 1:
                    break
            else:
                if j not in answer:
                    answer.append(visited.pop(visited.index(j)))
                    G[answer[-1]] = [0] * V
                    break

    print(f"#{test_case + 1}", *[a + 1 for a in answer])
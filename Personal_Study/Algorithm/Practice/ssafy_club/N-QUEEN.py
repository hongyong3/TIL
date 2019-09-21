def nqueen(sol, N):
    global count
    if len(sol) == N:
        count += 1
        print(count, sol)
        return 0
    candidate = list(range(N))
    for i in range(len(sol)):
        if sol[i] in candidate:
            candidate.remove(sol[i])
        distance = len(sol) - i
        if sol[i] + distance in candidate:
            candidate.remove(sol[i] + distance)
        if sol[i] - distance in candidate:
            candidate.remove(sol[i] - distance)
    if candidate != []:
        for i in candidate:
            sol.append(i)
            nqueen(sol, N)
            sol.pop()
    else:
        return 0

import sys
sys.stdin = open("N-QUEEN_input.txt", "r")
T = int(input())
count = 0
for test_case in range(T):
    N = int(input())
    table = [[0 for _ in range(8)] for _ in range(8)]
    nqueen([test_case], N)
if count == 0:
    print("No solution")
else:
    print(count)
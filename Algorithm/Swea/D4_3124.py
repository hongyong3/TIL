import sys
sys.stdin = open("D4_3124_input.txt", "r")

def findSet(x):
    if x == p[x]:
        return x
    return findSet(p[x])

def mst():
    global V
    count, total, i = 0, 0, 0
    while count < V:
        p1 = findSet(data[i][0])
        p2 = findSet(data[i][1])
        if p1 != p2:
            total += data[i][2]
            count += 1
            p[p2] = p1
        i += 1
    return total

T = int(input())
for test_case in range(T):
    V, E = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(E)]
    data.sort(key=lambda x: x[2])
    p = list(range(V + 1))
    print("#{} {}".format(test_case + 1, mst()))
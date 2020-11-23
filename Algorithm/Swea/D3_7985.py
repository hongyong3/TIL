import sys
sys.stdin = open("D3_7985_input.txt", "r")

def solve(s, e, depth):
    global N
    if depth > N:
        return
    m = (e - s) // 2
    tree[depth].append(data[m])
    solve(m - s, m, depth + 1)
    solve(m, e, depth + 1)


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [[] for _ in range(N)]
    print(data)
    # solve(0, 2 ** N - 1, 0)
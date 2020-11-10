import sys
sys.stdin = open("D3_7985_input.txt", "r")

def solve(s, e, d):
    global N
    if  d > N:
        return
    mid = (e - s) // 2


T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    tree = [pow(2, i) for i in range(11)]
    for i in range(tree[N] - 1):
        tree[i] = data[i]
    
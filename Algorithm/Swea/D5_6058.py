import sys
sys.stdin = open("D5_6058_input.txt", "r")

def solve(n, nn, b):
    tree[n][nn] = b
    if tree[n][nn] > 250:
        tree[n][nn] -= 250

T = int(input())
for test_case in range(T):
    B, L, N = map(int, input().split())
    tree = [[0] + [0] * (i * (i + 1) // 2) for i in range(L + 1)]10

    solve(1, 1, B * 750)

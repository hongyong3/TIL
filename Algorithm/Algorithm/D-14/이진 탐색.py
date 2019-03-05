import sys
sys.stdin = open("이진 탐색_input.txt", "r")

def inorder(node):
    global val, N
    if node <= N:
        inorder(node * 2)
        table[node] = val
        val += 1
        inorder(node * 2 + 1)

T = int(input())
for test_case in range(T):
    N = int(input())
    table = [0] * (N+1)
    val = 1
    inorder(1)
    print("#{} {} {} ".format(test_case + 1, table[1], table[N//2]))
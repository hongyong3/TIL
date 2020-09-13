import sys
sys.stdin = open("D4_3289_input.txt", "r")

def solve(n):
    if mat[n] == n:
        return n
    mat[n] = solve(mat[n])
    return mat[n]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    mat = [_ for _ in range(N + 1)]
    mat = ''
    for _ in range(M):
        a, b, c = map(int, input().split())
        temp1 = solve(b)
        temp2 = solve(c)
        if a == 0:
            mat[temp1] = temp2
            print(mat)
        else:
            if temp1 == temp2:
                mat += '1'
            else:
                mat += '0'

    print("#{} {}".format(test_case + 1, mat))
import sys
sys.stdin = open("[TST] 더하기_input.txt", "r")

def DFS(no, nsum):  # N개 중 M개를 고르는 조합
    global flag
    if flag or nsum > K:
        return
    if no >= N:
        if nsum == K:
            flag = 1
        return
    DFS(no + 1, nsum + data[no])
    DFS(no + 1, nsum)

# def DFS(no, nsum):
#     global flag
#     if nsum == K:
#         flag = 1
#         return
#     if nsum > K or flag:
#         return
#     if no >= N:
#         return
#     DFS(no + 1, nsum + data[no])
#     DFS(no + 1, nsum)

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    data = list(map(int, input().split()))
    rec = [0] * N
    flag = 0
    DFS(0, 0)

    if flag:
        print("YES")
    else:
        print("NO")
import sys
sys.stdin = open("[TEST] 도자기_input.txt", "r")

def DFS(idx, count, start): # 중복조합
    global ans
    if count >= M:
        if check not in ans:
            ans.append(check[:])
        return

    if idx >= N:
        return

    for i in range(start, N):
        check[idx] = data[i]
        DFS(idx + 1, count + 1,i + 1)

T = int(input())
for test_case in range(1):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))

    check = [0] * N
    ans = []
    answer = []

    DFS(0, 0, 0)
    print(ans)
    # print(len(ans))

    # [[1, 3, 0, 0, 0], [1, 2, 0, 0, 0], [1, 1, 0, 0, 0], [3, 2, 0, 0, 0], [3, 1, 0, 0, 0], [3, 3, 0, 0, 0], [2, 1, 0, 0, 0], [2, 3, 0, 0, 0]]
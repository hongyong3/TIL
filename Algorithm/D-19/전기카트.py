import sys
sys.stdin = open("전기카트_input.txt", "r")
T = int(input())
def perm(n, k, sum):
    global ans
    if sum > ans:
        return

    if n == k:
        sum += data[A[k - 1]][A[k]]
        if ans > sum:
            ans = sum

    for i in range(k, n):
        A[k], A[i] = A[i], A[k]
        perm(n, k + 1, sum + data[A[k - 1]][A[k]])
        A[k], A[i] = A[i], A[k]

for test_case in range(T):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    ans = float('inf')
    A = [_ for _ in range(N)] + [0]
    perm(N, 1, 0)

    print("#{} {}".format(test_case+1, ans))

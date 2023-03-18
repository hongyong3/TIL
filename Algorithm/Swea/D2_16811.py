import sys
sys.stdin = open("D2_16811_input.txt", "r")

'''
(1)N개의 당근을 주문하면 대, 중, 소 상자로 구분해 포장해야 한다.
(2)같은 크기의 당근은 같은 상자에 들어있어야 한다.
(3)비어 있는 상자가 있으면 안 된다.
(4)한 상자에 N/2개(N이 홀수면 소수점 버림)를 초과하는 당근이 있어서도 안 된다.
(5)앞의 조건을 만족하면서도, 각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 한다.
'''
T = int(input())
for test_case in range(T):
    N = int(input())
    arr = sorted(list(map(int, input().split())))
    ans = float('inf')
    for i in range(1, N - 1):
        for j in range(i + 1, N):
            A = arr[:i]
            B = arr[i : j]
            C = arr[j:]
            if A[- 1] == B[0] or B[- 1] == C[0]:
                continue
            if len(A) * len(B) * len(C) == 0:
                continue
            if max(len(A), len(B), len(C)) > N // 2:
                continue
            ans = min(ans, max(abs(len(A) - len(B)), abs(len(B) - len(C)), abs(len(C) - len(A))))
    if ans == float('inf'):
        ans = - 1
    print("#{} {}".format(test_case + 1, ans))
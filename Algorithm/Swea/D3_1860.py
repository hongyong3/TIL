import sys
sys.stdin = open("D3_1860_input.txt", "r")


def solve():
    T = int(input())


for test_case in range(T):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    data = sorted(data)
    ans = 'Possible'
    if min(data) < M:
        ans = 'Impossible'
    else:
        pass
    print("#{} {}".format(test_case + 1, ans))
import sys
sys.stdin = open("D4_19004_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    num = set()
    arr = []
    for _ in range(N):
        data = list(map(int, input().split()))
        arr.append(data)
        for i in data:
            num.add(i)
    if K != len(num):
        ans = - 1
    else:
        ans = 0
    print(ans)

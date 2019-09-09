import sys
sys.stdin = open("D3_3809_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = []
    if N < 20:
        data = list(map(int, input().split()))
    else:
        ans = [list(map(int, input().split())) for _ in range(N // 20)]
        for i in ans:
            data.append(i)
    print(data)
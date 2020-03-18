import sys
sys.stdin = open("D2_4861_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    dataT = [''.join(x) for x in zip(*data)]
    ans = ''
    for x, y in zip(data, dataT):
        i = 0
        while i < N - M + 1:
            if x[i: M + i] == x[i: M + i][:: - 1]:
                ans += x[i: M + i]
                break
            if y[i: M + i] == y[i: M + i][:: - 1]:
                ans += y[i: M + i]
                break
            i += 1
        if ans:
            print("#{} {}".format(test_case + 1, ans))
            break
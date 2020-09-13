import sys
sys.stdin = open("D5_1247_input.txt", "r")

def solve(n, k, total):
    global mat
    if total > ans:
        return
    if n == k:
        total += (abs(data3[- 2][0] - data3[- 1][0]) + abs(data3[- 2][1] - data3[- 1][1]))
        if ans > total:
            ans = total
    else:
        for i in range(k, n):
            data3[i], data3[k] = data3[k], data3[i]
            a = (abs(data3[k - 1][0] - data3[k][0]) + abs(data3[k - 1][1] - data3[k][1]))
            solve(n, k + 1, total + a)
            data3[i], data3[k] = data3[k], data3[i]

T = int(input())
for test_case in range(10):
    N = int(input())
    data = list(map(int, input().split()))
    company = [data.pop(0), data.pop(0)]
    home = [data.pop(0), data.pop(0)]
    data2 = [[data[i], data[i + 1]] for i in range(0, len(data), 2)]
    data3 = [company] + data2 + [home]
    mat = float('inf')
    solve(N + 1, 1, 0)
    print('#{} {}'.format(test_case + 1, mat))
import sys
sys.stdin = open("D4_3289_input.txt", "r")

def solve(n):
    if arr[n] == n:
        return n
    arr[n] = solve(arr[n])
    return arr[n]

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [_ for _ in range(N + 1)]
    ans = ''
    for _ in range(M):
        a, b, c = map(int, input().split())
        temp1 = solve(b)
        temp2 = solve(c)
        if a == 0:
            arr[temp1] = temp2
            print(arr)
        else:
            if temp1 == temp2:
                ans += '1'
            else:
                ans += '0'

    print("#{} {}".format(test_case + 1, ans))
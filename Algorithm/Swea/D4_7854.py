import sys
sys.stdin = open("D4_7854_input.txt", "r")

num = [[1, 2, 5], [10, 20, 25, 50], [100, 125, 200, 250, 500]]
def solve(n, arr):
    global ans
    for i in arr:
        if n >= i:
            ans += 1
        else:
            break

T = int(input())
for test_case in range(T):
    N = int(input())
    lenN = len(str(N))
    ans = 0

    if lenN == 1:
        solve(N, num[0])

    elif lenN == 2:
        ans += 3
        solve(N, num[1])

    else:
        ans += 7 + (lenN - 3) * 5
        solve(int(str(N)[:3]), num[2])
    print("#{} {}".format(test_case + 1, ans))
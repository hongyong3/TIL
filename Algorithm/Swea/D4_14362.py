import sys
sys.stdin = open("D4_14362_input.txt", "r")

# 122 / 125
dx = [1, 0, - 1, 0]
dy = [0, 1, 0, - 1]
T = int(input())
for test_case in range(T):
    command = input()
    x, y, k, ans = 0, 0, 0, 0
    arr = set()
    for _ in range(4):
        for i in command:
            if i == 'S':
                x += dx[k]
                y += dy[k]
                ans = max(ans, x ** 2 + y ** 2)
            elif i == 'R':
                k = (k - 1) % 4
            elif i == 'L':
                k = (k + 1) % 4
        arr.add(ans)
    if len(arr) == 4:
        ans = 'oo'
    print("#{} {}".format(test_case + 1, ans))
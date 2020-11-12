import sys
sys.stdin = open("D3_6853_input.txt", "r")

T = int(input())
for test_case in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())
    ans1, ans2, ans3 = 0, 0, 0

    for _ in range(N):
        x, y = map(int, input().split())
        if x1 < x < x2 and y1 < y < y2:
            ans1 += 1
        elif not (x1 <= x <= x2 and y1 <= y <= y2):
            ans3 += 1
        else:
            ans2 += 1
    print("#{} {} {} {}".format(test_case + 1, ans1, ans2, ans3))
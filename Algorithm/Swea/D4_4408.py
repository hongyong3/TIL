import sys
sys.stdin = open("D4_4408_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    room, ans = [0] * 201, 0
    for i in range(N):
        a, b = map(int, input().split())
        if a % 2 == 1: a += 1
        if b % 2 == 1: b += 1
        if a > b: a, b = b, a
        for j in range((a // 2), (b // 2) + 1):
            room[j] += 1
    print("#{} {}".format(test_case + 1, max(room)))
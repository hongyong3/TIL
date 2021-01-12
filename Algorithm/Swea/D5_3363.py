import sys
sys.stdin = open("D5_3363_input.txt", "r")

# Runtime Error...
# T = int(input())
# for test_case in range(T):
#     N = int(input())
#     arr, cnt = [], 0
#     for _ in range(N):
#         x, y, z = map(int, input().split())
#         arr.append((x, y, z))
#         if cnt < y:
#             cnt = y
#     num = [0] * (cnt + 1)
#
#     for a, b, c in arr:
#         for i in range(a, b + 1, c):
#             num[i] += 1
#
#     for i in range(1, cnt + 1):
#         if num[i] % 2:
#             print("#{} {} {}".format(test_case + 1, i, num[i]))
#             break
#     else:
#         print("#{} no corruption".format(test_case + 1))


T = int(input())
for test_case in range(T):
    N = int(input())
    arr, ans = [], 0
    for _ in range(N):
        x, y, z = map(int, input().split())
        arr.append((x, y, z))
        for i in range(x, y + 1, z):
            ans ^= i
    if not ans:
        print("#{} no corruption".format(test_case + 1))
    else:
        cnt = 0
        for j in arr:
            if j[0] <= ans <= j[1]:
                if not (ans - j[0]) % j[2]:
                    cnt += 1
        print("#{} {} {}".format(test_case + 1, ans, cnt))
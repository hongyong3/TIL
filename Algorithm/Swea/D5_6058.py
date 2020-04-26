import sys
sys.stdin = open("D5_6058_input.txt", "r")

# 재귀함수를 이용하면 runtime Error 예상...
# 와인 전달할 때 증가하는 값을 코드화하기
# def solve(n, nn, b):
#     tree[n][nn] += b
#     if tree[n][nn] > 250:
#         tree[n][nn] -= 250
#     if n == L:
#         return
#     solve(n + 1, nn, (b - 250) / 3)
#     solve(n + 1, nn + 1, (b - 250) / 3)
#     solve(n + 1, nn + 2, (b - 250) / 3)
#
# T = int(input())
# for test_case in range(T):
#     B, L, N = map(int, input().split())
#     tree = [[0] + [0] * (i * (i + 1) // 2) for i in range(L + 1)]
#
#     solve(1, 1, B * 750)
#     if tree[L][N] >= 250:
#         print("#{} {}".format(test_case + 1, 250))
#     else:
#         print("#{} {}".format(test_case + 1, tree[L][N]))

T = int(input())
for test_case in range(T):
    B, L, N = map(int, input().split())
    c = [[0] + [0] * (i * (i + 1) // 2) for i in range(L + 1)]
    c[1][1] = B * 750
    for i in range(1, L):
        ln = 1
        for j in range(1, (i * (i + 1) // 2) + 1):
            if j > ln + (ln * (ln - 1) / 2):
                ln += 1
            if c[i][j] > 250:
                c[i + 1][j] += (c[i][j] - 250) / 3
                c[i + 1][j + ln] += (c[i][j] - 250) / 3
                c[i + 1][j + ln + 1] += (c[i][j] - 250) / 3
                c[i][j] = 250
    print("#{} {}".format(test_case + 1, c[L][N] if c[L][N] <= 250 else 250))
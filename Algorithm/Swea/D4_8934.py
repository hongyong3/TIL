import sys
sys.stdin = open("D4_8934_input.txt", "r")

# T = int(input())
# for test_case in range(T):
#     s = input()
#     rs = s[::- 1]
#     ans = "YES"
#     if s == rs:
#         ans = "NO"
#     print("#{} {}".format(test_case + 1, ans))

T = int(input())
for test_case in range(T):
    s = input()
    ans = "YES"
    a, b, c = s.count('a'), s.count('b'), s.count('c')

    if max(max(a, b), c) - min(min(a, b), c) > 1:
        ans = "NO"
    print("#{} {}".format(test_case + 1, ans))

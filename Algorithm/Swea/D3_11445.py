import sys
sys.stdin = open("D3_11445_input.txt", "r")

T = int(input())
for test_case in range(T):
    p, q = input().strip(), input().strip()
    ans = 'Y'
    if len(q) - len(p) == 1 and p == q[: - 1] and q[- 1] == 'a':
        ans = 'N'
    print("#{} {}".format(test_case + 1, ans))
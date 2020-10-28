import sys
sys.stdin = open("D2_1285_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    ans = []
    for i in data:
        ans.append(abs(i))
    ans.sort()
    print("#{} {} {}".format(test_case + 1, ans[0], ans.count(ans[0])))
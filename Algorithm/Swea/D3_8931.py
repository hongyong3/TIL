import sys
sys.stdin = open("D3_8931_input.txt", "r")

T = int(input())
for test_case in range(T):
    K = int(input())
    ans = []
    for i in range(K):
        data = int(input())
        ans.append(data) if data else ans.pop()
    print("#{} {}".format(test_case + 1, sum(ans)))
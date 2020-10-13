import sys
sys.stdin = open("D3_2386_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = []
    for i in range(N):
        n = int(input())
        if n not in ans:
            ans.append(n)
        else:
            ans.remove(n)
    print("#{} {}".format(test_case + 1, len(ans)))
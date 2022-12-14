import sys
sys.stdin = open("D3_15868_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    ans = "no"
    for _ in range(N):
        data = list(input())
        a = int(data[0])
        for j in range(1, M):
            if a == int(data[j]):
                a = 0 if a == 1 else 1
            else:
                a = 1
        if not a:
            break
    else:
        ans = "yes"
    print("#{} {}".format(test_case + 1, ans))
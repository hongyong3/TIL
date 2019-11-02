import sys
sys.stdin = open("D4_4259_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, data, ans = int(input()), input().split(), 0
    # data = input().split()
    # ans = 0
    for i in range(N):
        ans += (int(data[i][:- 1]) ** int(data[i][- 1]))
    print("#{} {}".format(test_case + 1, ans))
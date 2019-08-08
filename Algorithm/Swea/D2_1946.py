import sys
sys.stdin = open("D2_1946_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = [list(map(str, input().split())) for _ in range(N)]
    print("#{}".format(test_case + 1))
    ans = []
    for i in range(len(data)):
        ans += data[i][0] * int(data[i][1])
    for i in range(0, len(ans), 10):
        print(''.join(ans[i: i + 10]))
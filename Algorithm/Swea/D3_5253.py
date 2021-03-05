import sys
sys.stdin = open("D3_5253_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    data = [input() for _ in range(N)]
    ans = 0
    for _ in range(M):
        temp = input()
        for i in data:
            if temp == i[:len(temp)]:
                ans += 1
                break
    print("#{} {}".format(test_case + 1, ans))
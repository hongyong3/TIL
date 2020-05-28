import sys
sys.stdin = open("D5_1814_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    # arr = [[0] * (N + 1) for _ in range(N + 1)]
    line = list(map(int, input().split()))
    row = list(map(int, input().split()))
    ans = 'Yes'
    if (line.count(N) and line.count(0)) or (line.count(0) and line.count(N)):
        ans = 'No'
    # ㄷㄷ;; 방법을 생각하자..
    print("#{} {}".format(test_case + 1, ans))
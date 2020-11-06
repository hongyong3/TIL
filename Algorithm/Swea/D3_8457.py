import sys
sys.stdin = open("D3_8457_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, B, E = map(int, input().split())
    data = list(map(int, input().split()))
    ans = 0
    for i in data:
        temp = (B // i - 1) * i
        for _ in range(3):
            temp += i
            if temp <= (B + E) and (B - E) <= temp:
                ans += 1
                break
    print("#{} {}".format(test_case + 1, ans))
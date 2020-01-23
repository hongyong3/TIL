import sys
sys.stdin = open("D4_5604_input.txt", "r")

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    data = list(map(str, list(range(A, B + 1))))
    ans = 0
    for i in data:
        for j in range(len(i)):
            ans += int(i[j])
    print("#{} {}".format(test_case + 1, ans))
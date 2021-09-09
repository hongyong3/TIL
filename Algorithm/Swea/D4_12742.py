import sys
sys.stdin = open("D4_12742_input.txt", "r")

T = int(input())
ans = []
for test_case in range(T):
    a, b = map(int, input().split())
    x = b - a
    ans.append("#{} {}".format(test_case + 1, x * (x + 1) // 2 - b))

for i in ans:
    print(i)
import sys
sys.stdin = open("D3_3750_input.txt", "r")

def minNumber(num):
    data = 0
    for i in num:
        data += int(i)
    if len(str(data)) == 1:
        ans.append(data)
    else:
        minNumber(list(str(data)))

T = int(input())
ans = []
for test_case in range(T):
    N = list(str(input()))
    minNumber(N)
for i in range(T):
    print("#{} {}".format(i + 1, ans[i]))
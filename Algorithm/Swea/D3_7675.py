import sys
sys.stdin = open("D3_7675_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    data = list(map(str, input().split()))
    print(data)
    ans = [0] * N
    k = 0
    for i in range(len(data)):
        if data[i][0].isupper():
            if data[i][-1].islower():
                ans[k] += 1
            elif len(data[i]) == 1:
                ans[k] += 1
            elif data[i][-1] == "." or data[i][-1] == "?" or data[i][-1] == "!":
                if data[i][-2].islower():
                    ans[k] += 1
                    k += 1
            else:
                continue
    print("#{} ".format(test_case + 1), end="")
    print(*ans)
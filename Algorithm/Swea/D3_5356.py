import sys
sys.stdin = open("D3_5356_input.txt", "r")

T = int(input())
for test_case in range(T):
    data = [list(map(str, input())) for _ in range(5)]
    ans = ""
    # print("#{} ".format(test_case + 1), end="")
    for i in range(5):
        for j in data[i]:
            ans += j
    print(ans)
            # print(data[j][i], end="")
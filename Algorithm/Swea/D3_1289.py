import sys
sys.stdin = open("D3_1289_input.txt", "r")

def solve(data, n):
    global count, ans
    if data == ans:
        return count
    for i in range(n, len(ans)):
        if ans[i] != data[i]:
            if ans[i] == '1':
                ans = ans[:i] + ans[i:].replace("1", "0")
            else:
                ans = ans[:i] + ans[i:].replace("0", "1")
            count += 1
            solve(data, i)

T = int(input())
for test_case in range(T):
    data = str(input())
    ans, count = '0' * len(data), 0
    solve(data, 0)
    print("#{} {}".format(test_case + 1, count))
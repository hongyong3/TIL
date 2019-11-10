import sys
sys.stdin = open("D4_3316_input.txt", "r")

def solve(idx, before):
    if idx == len(data):
        return 1
    ans = case[idx][before]
    if ans != - 1:
        return ans
    people = data[idx] - 'A'
    for i in range(1, 16):
        if (before & i) and ((1 << people) & i):
            ans = (ans + solve(idx + 1, i)) % 1000000007
    return ans % 1000000007


T = int(input())
for test_case in range(T):
    data = str(input())
    case = [[0] * 10000] * 16
    print("#{} {}".format(test_case + 1, solve(0, 1)))
import sys
sys.stdin = open("D4_4530_input.txt", "r")

def solve(num):
    result = 0
    l = len(str(num))
    n = str(num)
    s = 0
    for i in range(l - 1, - 1, - 1):
        val = int(n[i])
        if val > 4:
            val = val - 1
        result += val * pow(9, s)
        s += 1
    return result - 1

T = int(input())
for test_case in range(T):
    A, B = map(int, input().split())
    if A < 0 and B > 0:
        ans = solve(abs(A)) + solve(abs(B)) + 1
    else:
        ans = solve(abs(B)) - solve(abs(A))
    print("#{} {}".format(test_case + 1, abs(ans)))
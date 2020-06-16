import sys
sys.stdin = open("D5_3977_input.txt", "r")

def solve(l, r):
    check = [True] * r
    cnt = 0
    for i in range(2, r):
        if i <= int(r ** 0.5):
            if check[i]:
                for j in range(i+i, r, i):
                    check[j] = False
    for i in range(l, r):
        if i % 4 == 1 and check[i]:
            cnt += 1
    return cnt

T = int(input())
for test_case in range(T):
    L, R = map(int, input().split())
    print("#{} {}".format(test_case + 1, solve(L, R)))
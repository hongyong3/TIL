import sys
sys.stdin = open("D3_14512_input.txt", "r")

from itertools import permutations
T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(permutations(arr))
    ans = 31

    for i in arr:
        num = i[0][0]
        temp = num + 1
        idx = 1
        while idx < N:
            if not (i[0][0] <= num <= i[0][1]):
                num = - 1
                break
            if i[idx][0] <= temp <= i[idx][1]:
                temp += 1
                idx += 1
            else:
                num += 1
                temp = num + 1
                idx = 1
        if num != - 1:
            ans = min(ans, num)
    if ans == 31:
        ans = - 1
    print("#{} {}".format(test_case + 1, ans))
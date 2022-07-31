import sys
sys.stdin = open("D3_14511_input.txt", "r")

import copy
def solve2(idx, lst, val):
    jdx = 1
    while True:
        if lst[idx + jdx] % 2 == val:
            lst.insert(idx, lst.pop(idx + jdx))
            break
        else:
            jdx += 1
    return jdx


def solve(lst, val):
    idx, res = 0, 0
    while idx < N:
        if idx % 2:
            if lst[idx] % 2 != val:
                res += solve2(idx, lst, val)
        else:
            if lst[idx] % 2 == val:
                res += solve2(idx, lst, (val + 1) % 2)
        idx += 1
    return res


T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans, odd, even = 0, 0, 0

    for i in arr:
        if i % 2:
            odd += 1
        else:
            even += 1

    if abs(odd - even) > 1:
        ans = - 1
    else:
        if N > 2:
            if odd == even:
                ans = min(solve(copy.deepcopy(arr), 0), solve(arr, 1))
            elif odd > even:
                ans = solve(arr, 0)
            else:
                ans = solve(arr, 1)
    print("#{} {}".format(test_case + 1, ans))
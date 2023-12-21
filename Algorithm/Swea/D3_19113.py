import sys
sys.stdin = open("D3_19113_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = []
    idx = 1
    while arr:
        if arr[0] == int(arr[idx] * 0.75):
            arr.pop(idx)
            ans.append(arr.pop(0))
            idx = 1
        else:
            idx += 1
    print("#{}".format(test_case + 1), *ans)
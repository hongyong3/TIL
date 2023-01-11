import sys
sys.stdin = open("D4_15942_input.txt", "r")

T = int(input())
for test_case in range(T):
    N, K = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    ans = 0
    print(arr)
    while arr:
        if len(arr) > 1:
            for i in range(len(arr)):
                if K < arr[i]:
                    ans += 1
                    K += arr[i - 1]
                    arr.pop(i - 1)
                    break
            else:
                if K < arr[- 1]:
                    ans = - 1
                    break
                else:
                    K -= arr[- 1]
                    arr.pop(- 1)
        else:
            if K < arr[- 1]:
                ans = - 1
                break
            else:
                K -= arr[- 1]
                arr.pop(- 1)
    print(arr)
    print(ans)
import sys
sys.stdin = open("D1_9367_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    ans = 0
    temp = 1
    c = arr[0]
    for i in arr[1:]:
        if c < i:
            c = i
            temp += 1
        else:
            if ans < temp:
                ans = temp
                c = i
                temp = 1
    else:
        if ans < temp:
            ans = temp
    print("#{} {}".format(test_case + 1, ans))
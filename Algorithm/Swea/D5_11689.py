import sys
sys.stdin = open("D5_11689_input.txt", "r")

# Runtime Error..?
arr = []
T = int(input())
for test_case in range(T):
    a, b = map(int, input().split())
    ans = 0

    if a == 1 or b == 1:
        ans = max(a, b) - 1

    else:
        while a != b:
            if a == 1 or b == 1:
                ans += max(a, b) - 1
                break

            if a > b:
                a -= b
            else:
                b -= a
            ans += 1

    # print("#{} {}".format(test_case + 1, ans))
    arr.append("#{} {}".format(test_case + 1, ans))
for i in arr:
    print(i)

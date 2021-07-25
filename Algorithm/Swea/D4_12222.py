import sys
sys.stdin = open("D4_12222_input.txt", "r")

# 7 // 15
T = int(input())
for test_case in range(T):
    S = input()
    lS = len(S)
    ans = 0
    a, idx = S[0], 1
    # arr = []
    while idx < lS:
        b = S[idx]
        if a == b:
            s = a + b
            if idx + 1 == lS:
                # arr.append(s)
                ans += 1
                break
            if a == S[idx + 1]:
                # arr.append(a)
                # arr.append(s)
                ans += 2
                if idx + 2 == lS:
                    break
                a = s
                idx += 2
            else:
                if idx + 2 == lS:
                    break
                if S[idx + 1] == S[idx + 2]:
                    # arr.append(a)
                    # arr.append(b + S[idx + 1])
                    ans += 2
                    a = b + S[idx + 1]
                    idx += 2
        else:
            if idx + 1 == lS:
                # arr.append(b)
                ans += 1
                break
            if b == S[idx + 1]:
                if not ans:
                    ans += 1
                    # arr.append(a)
                # arr.append(b + S[idx + 1])
                ans += 1
                idx += 2
                if idx + 1 >= lS:
                    break
                a = b + S[idx + 1]
            else:
                if not ans:
                    ans += 1
                    # arr.append(a)
                # arr.append(b)
                a = b
                ans += 1
                idx += 1
    # print(arr)
    print("#{} {}".format(test_case + 1, ans))
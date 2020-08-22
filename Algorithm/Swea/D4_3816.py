import sys
sys.stdin = open("D4_3816_input.txt", "r")

T = int(input())
for test_case in range(T):
    s1, s2 = input().split()
    ans, len1, len2, s1Alpha, s2Alpha = 0, len(s1), len(s2), [0] * 27, [0] * 27

    for i in s1:
        s1Alpha[ord(i) - 97] += 1

    s, e = 0, 0
    while s < len2:
        if e - s == len1:
            if s1Alpha == s2Alpha:
                ans += 1
            s2Alpha[ord(s2[s]) - 97] -= 1
            s += 1
        else:
            if e < len2:
                s2Alpha[ord(s2[e]) - 97] += 1
            e += 1
    print("#{} {}".format(test_case + 1, ans))
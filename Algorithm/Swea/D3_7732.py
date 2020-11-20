import sys
sys.stdin = open("D3_7732_input.txt", "r")

T = int(input())
for test_case in range(T):
    h1, m1, s1 = map(int, input().split(':'))
    h2, m2, s2 = map(int, input().split(':'))
    t1 = h1 * 3600 + m1 * 60 + s1
    t2 = h2 * 3600 + m2 * 60 + s2
    t = t2 - t1 + 86400 if t1 > t2 else t2 - t1

    ans = ''
    if t // 3600 < 10:
        ans += '0' + str(t // 3600)
    else:
        ans += str(t // 3600)

    if (t % 3600) // 60 < 10:
        ans += ':0' + str((t % 3600) // 60)
    else:
        ans += ':' + str((t % 3600) // 60)

    if (t % 3600) % 60 < 10:
        ans += ':0' + str((t % 3600) % 60)
    else:
        ans += ':' + str((t % 3600) % 60)
    print("#{} {}".format(test_case + 1, ans))
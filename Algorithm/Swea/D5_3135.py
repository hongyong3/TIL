import sys
sys.stdin = open("D5_3135_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    ans = []
    words = []
    for _ in range(N):
        p, s = input().split()
        if p == '1':
            words.append(s)
        else:
            cnt = 0
            for i in words:
                if s == i[:len(s)]:
                    cnt += 1
            ans.append(cnt)
    print("#{}".format(test_case + 1), *ans)
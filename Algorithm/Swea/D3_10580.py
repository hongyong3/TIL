import sys
sys.stdin = open("D3_10580_input.txt", "r")

T = int(input())
for test_case in range(T):
    N = int(input())
    p, cp, c, cDot, chk = 0, 0, 0, set(), set() # 평행, 교차-평행O, 교차-평행X, 교차-평행 확인
    for i in range(N):
        a, b = map(int, input().split())
        if a == b:  # 평행이면
            p += 1
        else:   # 교차이면
            if a - b not in cDot:  # 평행X이면
                cDot.add(a - b)
                c += 1
            else:   # 평행이면
                if a - b not in chk:
                    cp += 1
                    chk.add(a - b)

    # print(p, cp, c) # 평행, 교차평행, 교차
    ans = p * cp
    if c:
        ans += (p * c) + c - 1
    # ans = (p * c) + c - 1 + (p * cp)
    print("#{} {}".format(test_case + 1, ans))
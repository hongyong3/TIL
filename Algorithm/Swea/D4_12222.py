import sys
sys.stdin = open("D4_12222_input.txt", "r")

def same(x):
    global ls, idx, ans, arr
    cnt = 2
    kdx = idx + 1
    while kdx < ls:
        idx += 1
        if x == S[kdx]:
            cnt += 1
            kdx += 1
        else:
            break
    m = cnt // 3
    n = cnt % 3
    ans += m * 2
    if n == 0:
        for i in range(m):
            arr.append(x)
            arr.append(x + x)
    elif n == 1:
        ans += 1
        for i in range(m):
            arr.append(x)
            arr.append(x + x)
        arr.append(x)
    else:
        ans += 1
        for i in range(m):
            arr.append(x + x)
            arr.append(x)
        arr.append(x + x)
        x += x
    return x

# 7 // 15
'''
    몫 = x // 3
    나머지 = x % 3
    갯수
    나머지 0 : 몫 * 2 : a = 'a'
    나머지 1 : 몫 * 2 + 1 : a = 'a'
    나머지 2 : 몫 * 2 + 1 : a = 'aa'
'''
T = int(input())
for test_case in range(1):
    S = input()
    ls = len(S)
    ans = 0
    a, idx = S[0], 1
    arr = []
    while idx < ls:
        b = S[idx]
        if a == b:  # 같은게 짝수개이면 [a, aa, a] 홀수개이면 [aa, a, aa]
            cnt = 2
            kdx = idx + 1
            a = same(a)
        else:

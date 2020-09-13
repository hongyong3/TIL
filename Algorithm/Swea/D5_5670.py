import sys
sys.stdin = open("D5_5670_input.txt", "r")

def solve(n):
    global check, mat
    if chk:
        chk = False
        n *= 2
        ans += 1
    else:
        temp = (G - n) / 2
        temp = int(temp) if temp == int(temp) else int(temp) + 1
        n += temp * 2
        ans += temp
    return n

T = int(input().replace('혻', ''))
for test_case in range(T):
    G, N = map(int, input().replace('혻', '').split())
    funxy = set()
    funa = set()
    check = True
    mat = 0

    for i in range(N):
        x1, y1, x2, y2 = map(int, input().replace('혻', '').split())

        if x1 == x2 or y1 == y2:
            if x1 == x2:
                funa.add(20000)
                funxy.add((20001, x1, float('inf')))
            if y1 == y2:
                funa.add(0)
                funxy.add((0, float('inf'), y1))
        else:
            a = (y2 - y1) / (x2 - x1)
            funa.add(a)
            funxy.add((a, x1 - (y1 / a), y1 - a * x1))

    if len(funa) == 1:
        fence = len(funxy) + 1
    else:
        check = False
        fence = 2 * len(funxy)
    while fence < G:
        fence = solve(fence)
    print("#{} {}".format(test_case + 1, mat))